# Python Automation Report

## Summary

This phase focused on transforming manual log analysis into reusable Python-based detection scripts.

The objective was to automate repetitive SOC analyst tasks and improve efficiency during triage.

---

## Scripts Developed

### 1. failed_logins.py

Purpose:

Detect failed SSH authentication attempts.

Input:

```text
logs/ssh-bruteforce/auth.log
```

Detection:

* Failed password attempts
* Invalid user attempts

Use case:

Quick identification of brute force attempts.

---

### 2. count_failed_logins_by_ip.py

Purpose:

Count failed SSH login attempts by source IP.

Input:

```text
logs/ssh-bruteforce/auth.log
```

Detection:

* Attacker frequency
* Top brute force sources

Use case:

Identify high-volume attacking IPs.

---

### 3. suspicious_web_requests.py

Purpose:

Detect suspicious HTTP requests and reconnaissance patterns.

Input:

```text
logs/web-enumeration/access.log
```

Detection:

* Gobuster activity
* Nmap user-agents
* OPTIONS
* PROPFIND
* POST
* Sensitive paths

Use case:

Detect directory brute forcing and service probing.

---

### 4. sudo_activity_parser.py

Purpose:

Detect privilege escalation and sudo activity.

Input:

```text
logs/ssh-bruteforce/auth.log
```

Detection:

* sudo usage
* root session openings

Use case:

Track post-authentication privilege activity.

---

## Benefits

Automation improved:

* Speed of analysis
* IOC extraction
* Reusability
* Detection consistency
* Analyst efficiency

---

## Evidence

Screenshots:

* `screenshots/python-automation/01-failed-logins-script.png`
* `screenshots/python-automation/02-count-failed-logins-by-ip.png`
* `screenshots/python-automation/03-suspicious-web-requests.png`
* `screenshots/python-automation/04-sudo-activity-parser.png`

Scripts:

* `scripts/ssh-bruteforce/failed_logins.py`
* `scripts/ssh-bruteforce/count_failed_logins_by_ip.py`
* `scripts/web-enumeration/suspicious_web_requests.py`
* `scripts/privilege-analysis/sudo_activity_parser.py`

---

## Conclusion

This phase demonstrates the transition from manual investigation to automated detection engineering.

These scripts provide a foundation for future SOC tooling and larger-scale log analysis.
