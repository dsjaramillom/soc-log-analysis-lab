# SOC Log Analysis Lab

A hands-on cybersecurity lab focused on attack simulation, log analysis, incident investigation, and detection automation.

This repository documents a complete attack lifecycle in a controlled lab environment using Kali Linux as the attacker and Ubuntu Server as the victim, following a SOC Tier 1 investigation workflow.

---

## Project Objective

The goal of this project was to simulate real-world attack scenarios, analyze their traces in logs, and automate parts of the detection process.

Main focus areas:

* Linux authentication log analysis
* Network reconnaissance
* SSH brute force detection
* Web enumeration analysis
* Apache access log investigation
* IOC extraction
* Detection engineering
* Incident documentation
* Python log automation

---

## Lab Architecture

```text
Kali Linux (Attacker) ---> Ubuntu Server (Victim)
```

Environment:

* Kali Linux
* Ubuntu Server
* VirtualBox Internal Network (`SOC-LAB`)
* NAT enabled for internet access

---

## Network Configuration

### Ubuntu Server

IP Address:

```text
192.168.56.10
```

---

### Kali Linux

IP Address:

```text
192.168.56.11
```

Validation:

* Successful ping between both machines
* Internal communication established

Evidence:

![Kali Network](screenshots/lab-setup/01-kali-network-config.png)

![Ubuntu Network](screenshots/lab-setup/02-ubuntu-network-config.png)

---

## Services Installed

### SSH

Purpose:

* Authentication analysis
* Brute force simulation
* Privileged activity tracking

Evidence:

![SSH Status](screenshots/lab-setup/04-ssh-service-status.png)

---

### Apache HTTP Server

Purpose:

* Web enumeration analysis
* HTTP log monitoring
* Suspicious request detection

Evidence:

![Apache Status](screenshots/lab-setup/03-apache-service-status.png)

---

## Open Ports Validation

Detected services:

* 22/tcp (SSH)
* 80/tcp (HTTP)

Evidence:

![Open Ports](screenshots/lab-setup/05-open-ports.png)

---

# Completed Phases

---

## Phase 1 — Infrastructure Setup

Completed:

* Ubuntu installation
* Kali installation
* VirtualBox network configuration
* Internal communication validation

Documentation:

* `lab-setup/kali-setup.md`
* `lab-setup/ubuntu-server-setup.md`
* `lab-setup/network-diagram.md`

---

## Phase 2 — Victim Preparation & Baseline

Completed:

* System updates
* SSH verification
* Apache verification
* Open ports validation
* Baseline log inspection

Evidence:

![Baseline Logs](screenshots/lab-setup/06-baseline-log-preview.png)

---

## Phase 3 — Reconnaissance with Nmap

Tool:

* Nmap

Techniques:

* Port scanning
* Service enumeration
* Version detection
* OS fingerprinting
* HTTP endpoint probing

Documentation:

* `reports/nmap-recon/incident-report.md`

Evidence:

* `screenshots/nmap-recon/`

MITRE ATT&CK:

* T1595 — Active Scanning
* T1046 — Network Service Discovery

---

## Phase 4 — SSH Brute Force Analysis

Tool:

* Hydra

Techniques:

* Invalid user attempts
* Failed authentication
* Successful login simulation
* Privilege escalation tracking

Documentation:

* `reports/ssh-bruteforce/incident-report.md`

Evidence:

* `screenshots/ssh-bruteforce/`

MITRE ATT&CK:

* T1110 — Brute Force
* T1078 — Valid Accounts

---

## Phase 5 — Web Enumeration Analysis

Tool:

* Gobuster

Techniques:

* Directory brute forcing
* Hidden endpoint discovery
* Sensitive path identification

Documentation:

* `reports/web-enumeration/incident-report.md`

Evidence:

* `screenshots/web-enumeration/`

MITRE ATT&CK:

* T1595.003 — Web Vulnerability Scanning

---

## Phase 6 — Manual Log Analysis

Manual investigation included:

* Failed SSH login analysis
* Successful login correlation
* Sudo activity review
* Nmap detection
* Gobuster detection
* Source IP correlation
* HTTP method analysis
* 404 burst analysis

Documentation:

* `notes/manual-log-analysis.md`

Evidence:

* `screenshots/manual-analysis/`

---

## Phase 7 — Python Automation

Custom detection scripts:

* `failed_logins.py`
* `count_failed_logins_by_ip.py`
* `suspicious_web_requests.py`
* `sudo_activity_parser.py`

Purpose:

Automate repetitive SOC analyst tasks.

Documentation:

* `reports/python-automation/automation-report.md`

Evidence:

* `screenshots/python-automation/`

---

## Phase 8 — Final Project Summary

Consolidated:

* Attack timeline
* IOC extraction
* MITRE ATT&CK mapping
* Detection opportunities
* Security recommendations
* Professional reflection

Documentation:

* `reports/final-project-summary/final-project-summary.md`

---

# Raw Evidence Collected

Preserved logs:

```text
logs/
├── syslog
├── nmap-recon/
│   └── nmap-scan.txt
├── ssh-bruteforce/
│   └── auth.log
└── web-enumeration/
    ├── access.log
    ├── error.log
    └── gobuster-results.txt
```

---

# Detection Scripts

```text
scripts/
├── privilege-analysis/
│   └── sudo_activity_parser.py
├── ssh-bruteforce/
│   ├── count_failed_logins_by_ip.py
│   └── failed_logins.py
└── web-enumeration/
    └── suspicious_web_requests.py
```

---

# Repository Structure

```text
soc-log-analysis-lab/
│   README.md
│
├── lab-setup/
├── logs/
├── notes/
├── reports/
├── screenshots/
└── scripts/
```

---

# Key Indicators of Compromise (IoCs)

Observed:

Source IP:

```text
192.168.56.11
```

User-agents:

* Gobuster
* Nmap Scripting Engine

Suspicious HTTP methods:

* OPTIONS
* PROPFIND
* POST

Sensitive paths:

* /server-status
* /.htaccess
* /.htpasswd
* /.hta

Authentication indicators:

* Invalid user david
* Multiple failed login attempts

Privilege indicators:

* Sudo activity
* Root session openings

---

# Skills Demonstrated

* SOC Tier 1 workflow
* Linux log analysis
* Threat detection
* IOC extraction
* Incident reporting
* MITRE ATT&CK mapping
* Python scripting
* Basic detection engineering
* Attack simulation
* Blue team fundamentals

---

# Current Training

* Cisco Junior Cybersecurity Analyst
* Linux log analysis
* SOC Tier 1 preparation
* Python for security automation

---

## Final Note

This project represents the beginning of my transition into cybersecurity.

It reflects practical experience in attack simulation, log analysis, threat detection, and security automation.

This is only the beginning.
