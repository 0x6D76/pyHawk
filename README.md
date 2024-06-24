# Objectives

To automate the initial reconnaissance process against a target, parse through the results and present only interesting & necessary information to the user

---

# Recommended Operations

1. Ensure all required tools are installed in the system
2. Map services to specialized tools or scans
3. Validate user supplied target address
4. Identify open ports on the target
5. Identify service, product & version details of the identified ports
6. Identify interesting information about the identified ports, using NMAP-NSE scripts
7. Identify interesting information about the identified ports, using specialized scans/tools
8. Identify well-known vulnerabilities on the identified ports, using NMAP-NSE scripts
9. Identify well-known vulnerabilities on the identified ports, using specialized scans/tools
10. Multi-thread operations post open ports identification to haste the operation
11. Log every step of the tool’s operation- both STDOUT and log file
12. Present a summary of the tool’s findings
13. Output the results into JSON format (JSON file)
14. Handle user-interrupt, Ctrl-C

---

# Anatomy of Tool’s Output

![pyHawk Output](img/pyHawk.jpg)

---

# Operation Flow

1. If Keyboard interrupt (Ctrl-C) was hit at any point during the operation, jump to  (13)
2. Validate number of arguments given
3. Validate given arguments (target address)
4. Validate all tools are installed
5. Identify open ports & filtered ports
6. Print a summary of identified ports
7. For each open port identified, run NSE script scan with ‘-sC’ and ‘--script=vuln’ flags
8. Parse the results & identify vital information from (6)
9. Print a summary of identified information from (7)
10. For each open port identified, run all scans mapped to the port in ‘serviceMap.json’
    1. If a tool is not present, add it the failed scans list
11. Parse the results & identify vital information from (9)
12. Print a summary of identified information (10)
13. Convert the host object into JSON format and save it to a file in CWD
14. Print a master summary of all the entire operation
15. Present the user with probable attack vectors
16. Exit the tool

---

# File Structure

```
pyHawk
|
|
|_ _ _ _ support
|		 |
|		 |_ _ _ _ target.py
|		 |
|		 |_ _ _ _ support.py
|		 |
|		 |_ _ _ _ pyLogger
|		 |        |
|		 |        |_ _ _ _ <tool files/dirs>
|		 |        |
|		 |        |_ _ _ _ returnCodes.py (edited)
|		 |
|		 |_ _ _ _ serviceMap.json
|		 |
|		 |_ _ _ _ services
|
|
|_ _ _ _ test
|        |
|        |_ _ _ _ pyHawkTest.py
|
|
|_ _ _ _ pyHawk.py
|
|_ _ _ _ README.md
```

---
