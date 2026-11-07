# Blue Team: Log Analysis & Detection

## The Pyramid of Pain
Learned how to prioritize threat indicators. Blocking IPs (bottom) causes zero pain. Detecting TTPs (top) forces attackers to rewrite their entire playbook.

## Windows Event IDs
- 4624: Successful login
- 4625: Failed login (Brute force indicator)
- 4688: Process creation

## Python Log Analyzer
Built a Python script (`log_analyzer.py`) that reads Linux `auth.log` files, extracts IPs from "Failed password" lines using Regex, and uses the `collections.Counter` module to trigger a CRITICAL ALERT if an IP exceeds 3 failed attempts.

### Output Proof:
- 🚨 [CRITICAL ALERT] Brute Force Detected from IP: 192.168.1.50 (Total Failures: 4)
- ✅ [INFO] Normal failed login from IP: 10.0.0.5 (Total Failures: 1)

