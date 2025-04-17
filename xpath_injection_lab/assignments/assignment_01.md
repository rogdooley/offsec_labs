
## **Blind XPath Injection to Enumerate Admins**

### Objective

Write a Python3 script that uses **blind XPath injection** to extract the usernames of all users with the role `admin`, using **HTTP status code 200 vs 401** as the response oracle.

---

## Target Summary

Your Flask app is still using an insecure XPath query like:

```python
xpath_query = f".//user[username/text()='{username}' and password/text()='{password}']"
```

That means any input you control in the `username` field gets inserted raw into an XPath expression.

---

## Goal

1. Extract the usernames of all users where `role = 'admin'`
    
2. Use `username` field for the injection payload
    
3. Use a static password like `x`
    
4. Infer success by detecting HTTP 200 vs 401
    
5. Output the discovered admin usernames
    

---

## XPath Injection Strategy

Use payloads that effectively test this logic:

```xpath
//user[substring(username/text(),1,1)='a' and role='admin']
```

You’ll inject this logic through the `username` field by **breaking out of the current string context**. Example injection (not full syntax):

```
' or substring(username[role='admin'],1,1)='a
```

But XPath syntax doesn't support that directly — you’ll need to iterate like this:

```
username = "' or substring(//user[role='admin'][1]/username/text(), 1, 1) = 'a"
```

You'll increment:

- The character index in `substring(...)`
    
- The user index in `[1]`, `[2]`, etc.
    

---

## Constraints

- Only extract `username`s of users where `role='admin'`
    
- Limit attempts to usernames up to 10 characters
    
- Allow indexing up to 10 users (20 if you want to overbuild)
    
- Only lowercase a–z usernames
    
- Ignore passwords entirely (they're irrelevant for the attack)
    

---

## Script Requirements

- Accept base URL with `--url`
    
- Save logs to `attack.log`
    
- Output discovered usernames at the end
    
- Implement logic to:
    
    - Loop over user index `[1]`, `[2]`, ...
        
    - For each, loop over char position `[1]`, `[2]`, ...
        
    - For each position, test `a`–`z`
        
    - Break when no character matches (end of string)
        

Place your script in:

```
offsec_labs/xpath_injection_lab/attacker_scripts/blind_xpath_exploit.py
```

---

## Example Command Line

```bash
python3 blind_xpath_exploit.py --url http://127.0.0.1:5000
```

---

Let me know if you'd like example pseudocode for the loop logic or an input/output format spec before diving in.