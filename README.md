# SOC Log Analysis Lab

A practical cybersecurity lab focused on log analysis, attack simulation, incident investigation, and defensive documentation.

This repository documents hands-on blue team exercises using a controlled lab environment with Linux servers and attack simulation through Kali Linux.

---

## Objective

The purpose of this project is to build practical Security Operations Center (SOC) skills by simulating attacks, analyzing logs, documenting incidents, and improving detection capabilities.

Main focus areas:

* Linux authentication log analysis
* SSH brute force detection
* Web server monitoring
* Incident triage and documentation
* Threat detection mapping
* Basic adversary emulation

---

## Lab Environment

### Infrastructure

* Attacker Machine: Kali Linux
* Target Machine: Ubuntu Server
* Services:

  * SSH
  * Apache

### Network Configuration

Lab setup screenshots:

![Kali Network](screenshots/lab-setup/01-kali-network-config.png)

![Ubuntu Network](screenshots/lab-setup/02-ubuntu-network-config.png)

---

## Services Validation

### Apache Service

![Apache Status](screenshots/lab-setup/03-apache-service-status.png)

### SSH Service

![SSH Status](screenshots/lab-setup/04-ssh-service-status.png)

### Open Ports

![Open Ports](screenshots/lab-setup/05-open-ports.png)

---

## Completed Labs

### Lab 01 — SSH Brute Force Analysis

Description:

Simulated SSH authentication attempts including:

* Invalid user login attempts
* Failed authentication attempts
* Successful login events
* Privilege escalation activity

Evidence:

![Kali Brute Force](screenshots/ssh-bruteforce/01-kali-bruteforce.png)

![Auth Log Evidence](screenshots/ssh-bruteforce/02-auth.log-report.png)

Documentation:

* Incident Report:
  `reports/ssh-bruteforce/incident-report.md`

---

## Repository Structure

```text
soc-log-analysis-lab/
├── lab-setup/
├── logs/
├── notes/
├── reports/
├── screenshots/
└── scripts/
```

---

## MITRE ATT&CK Techniques Covered

* T1110 — Brute Force
* T1078 — Valid Accounts

---

## Roadmap

Upcoming labs:

* Apache log analysis
* Web enumeration detection
* Suspicious HTTP requests
* Fail2Ban implementation
* SSH key authentication hardening
* Sigma detection rules
* Bash log parsing automation

---

## Analyst Notes

This repository is part of my practical transition into cybersecurity, focused on SOC analysis, threat detection, and incident response.

Current focus:

* Cisco CCST Cybersecurity
* Linux log analysis
* Blue team fundamentals
* SOC analyst preparation
