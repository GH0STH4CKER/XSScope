````markdown
# XSScope

> **A simple XSS reflection checker tool**

---

### Description

XSScope is a lightweight command-line tool designed to quickly check if a target website reflects an XSS payload — helping you identify potential cross-site scripting vulnerabilities. It uses an external API to perform the scan and displays clear results in your terminal with colored output.

**This is a basic tool intended for quick checks and educational purposes.** It is *not* a full-featured vulnerability scanner or exploit framework.

---

### Features

- Checks your internet connection before scanning  
- Verifies target site accessibility  
- Queries an API to detect reflected XSS payloads  
- Displays the search URL pattern found on the target site  
- Colorful terminal output for easy reading  

---

### Requirements

- Python 3  
- Modules listed in `requirements.txt`:  
  - `requests`  
  - `colorama`  

---

### Installation

1. Clone or download the repository.  
2. Install dependencies:  
   ```bash
   pip3 install -r requirements.txt
````

3. Make the script executable:

   ```bash
   chmod +x XSScope.py
   ```

---

### Usage

Run the tool with the target URL using the `-u` option:

```bash
./XSScope.py -u https://targetsite.com
```

Example output:

```
   _  __________                 
  | |/_/ __/ __/______  ___  ___ 
 _>  <_\ \_\ \/ __/ _ \/ _ \/ -_)
/_/|_/___/___/\__/\___/ .__/\__/ 
                     /_/           
-------------------------------------
 [*] Developed by GH0STH4CKER
--------------------------------------

[*] Checking internet connection...
[+] Internet connection is ON
[*] Checking site accessibility: https://targetsite.com
[+] Site is accessible
[*] Querying XSS check API for: https://targetsite.com
[+] Search URL pattern found:
    https://targetsite.com/search?q=<payload>
[+] XSS payload was reflected in the response! Potential vulnerability detected.
```

---

### Disclaimer

This tool is intended for authorized testing and educational use only. Use it responsibly and do not scan websites without permission.


