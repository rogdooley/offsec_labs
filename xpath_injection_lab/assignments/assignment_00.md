
## **Build a Vulnerable XPath Injection Web Application**

## Objective

Create a Flask-based web application that simulates a vulnerable login system. The backend should authenticate users by evaluating user-provided credentials against an XML file using an **unsafe XPath query**. This sets the foundation for exploiting XPath injection in future assignments.

## Requirements

The application must:

- Accept POST requests to `/login` with fields `username` and `password`
- Use an XML file (`users.xml`) as a backend "database" for users
- Construct an XPath query directly using the input values (no sanitization)
- Return HTTP 200 when a user is found
- Return HTTP 401 when no matching user is found
- Set a session variable (`logged_in`) upon successful authentication
- Serve a basic login form at `/` using a template file

## File Structure

Place this lab under:

```

offsec_labs/xpath_injection_lab/

```

Within that, structure the project like so:

```
xpath_injection_lab/ ├── target_app/ │ ├── app.py # Flask app with vulnerable logic │ ├── users.xml # XML file storing user data │ └── templates/ │ └── login.html # Basic login form (HTML) ├── attacker_scripts/ │ └── blind_xpath_exploit.py # (To be created in Assignment 1) ├── requirements.txt # Contains Flask and lxml └── README.md # Project documentation

````

## Sample XML (`users.xml`)

Start with the following:

```xml
<users>
  <user>
    <username>alice</username>
    <password>W0nd3rL@nd!</password>
    <role>user</role>
  </user>
  <user>
    <username>bob</username>
    <password>Bui1dM3$tr0</password>
    <role>user</role>
  </user>
  <user>
    <username>charlie</username>
    <password>Ch@c0L8Riv3r</password>
    <role>admin</role>
  </user>
  <user>
    <username>dave</username>
    <password>H@L9k_Sys</password>
    <role>user</role>
  </user>
  <user>
    <username>eve</username>
    <password>Ev3Sp00f!</password>
    <role>user</role>
  </user>
  <user>
    <username>frank</username>
    <password>Pun1sh3r#99</password>
    <role>admin</role>
  </user>
  <user>
    <username>grace</username>
    <password>H0pp3r_C0d3</password>
    <role>user</role>
  </user>
  <user>
    <username>henry</username>
    <password>F0rd_M0d3lT!</password>
    <role>user</role>
  </user>
  <user>
    <username>ivy</username>
    <password>Gr33nL3@f*</password>
    <role>user</role>
  </user>
  <user>
    <username>jack</username>
    <password>Bean$talk42</password>
    <role>user</role>
  </user>
  <user>
    <username>karen</username>
    <password>LetM3Sp34k!</password>
    <role>user</role>
  </user>
  <user>
    <username>leo</username>
    <password>DaV1nci#C0d3</password>
    <role>user</role>
  </user>
  <user>
    <username>mia</username>
    <password>Pr1nc3ssD1@ry</password>
    <role>user</role>
  </user>
  <user>
    <username>nick</username>
    <password>FurY!S3cr3ts</password>
    <role>admin</role>
  </user>
  <user>
    <username>olivia</username>
    <password>W1ldC@t#22</password>
    <role>user</role>
  </user>
  <user>
    <username>peter</username>
    <password>P@nSh@d0w</password>
    <role>user</role>
  </user>
  <user>
    <username>quinn</username>
    <password>J0ker_L@ugh!</password>
    <role>user</role>
  </user>
  <user>
    <username>rachel</username>
    <password>Fr13nds4L!fe</password>
    <role>user</role>
  </user>
  <user>
    <username>steve</username>
    <password>CapT@Rog3rs</password>
    <role>admin</role>
  </user>
  <user>
    <username>tara</username>
    <password>W1zz@rdM@g1c</password>
    <role>user</role>
  </user>
</users>

````

## Key Notes

- Use `lxml.etree` for XML parsing and XPath execution
    
- Build the XPath query unsafely, for example:
    

```python
xpath_query = f".//user[username/text()='{username}' and password/text()='{password}']"
result = tree.xpath(xpath_query)
```

- Use Flask sessions (`session['logged_in'] = True`) to simulate login state
    
- Add a `secret_key` to enable Flask session handling
    

## Success Criteria

- Submitting valid credentials returns a 200 OK and changes session state
    
- Submitting invalid credentials returns 401 Unauthorized
    
- Manual testing possible via HTML login form at `/`
    
- App must run locally using:
    
    ```bash
    python3 app.py --port 5000
    ```
    

## Completion Status

Once the application is functional and exhibits distinct behavior based on XPath query matches, Assignment 0 is complete and you can proceed to blind XPath exploitation in Assignment 1.

