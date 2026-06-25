# Final Project Summary — SOC Log Analysis Lab

## Executive Summary

This project simulated a complete attack lifecycle in a controlled lab environment using Kali Linux as the attacker and Ubuntu Server as the victim.

The objective was to understand how attacks develop from reconnaissance to exploitation, how they leave traces in logs, and how a SOC analyst can investigate and automate detection.

Throughout the project, multiple attack scenarios were executed, documented, analyzed manually, and later automated using Python.

---

## Attack Timeline

### Phase 1 — Infrastructure Setup

Environment preparation:

* Kali Linux deployment
* Ubuntu Server deployment
* VirtualBox networking configuration
* Internal communication validation

---

### Phase 2 — Victim Preparation

Services prepared:

* SSH
* Apache HTTP Server

Baseline logs reviewed:

* auth.log
* access.log
* syslog

---

### Phase 3 — Reconnaissance

Tool used:

* Nmap

Techniques:

* Port scanning
* Service detection
* Version enumeration
* OS fingerprinting

---

### Phase 4 — SSH Brute Force

Tool used:

* Hydra

Techniques:

* Invalid user attempts
* Failed password attempts
* Successful authentication simulation

---

### Phase 5 — Web Enumeration

Tool used:

* Gobuster

Techniques:

* Directory brute forcing
* Sensitive path discovery
* Endpoint enumeration

---

### Phase 6 — Manual Log Analysis

Techniques:

* Failed login review
* Successful login correlation
* Privilege escalation detection
* HTTP method analysis
* Source IP analysis

---

### Phase 7 — Python Automation

Custom scripts developed:

* failed_logins.py
* count_failed_logins_by_ip.py
* suspicious_web_requests.py
* sudo_activity_parser.py

Purpose:

Automate repetitive log analysis tasks.

---

## Indicators of Compromise (IoCs)

Identified during the project:

Source IP:

192.168.56.11

Suspicious user-agents:

* Gobuster
* Nmap Scripting Engine

Suspicious methods:

* OPTIONS
* PROPFIND
* POST

Suspicious paths:

* /server-status
* /.htaccess
* /.htpasswd
* /.hta

Authentication indicators:

* Invalid user david
* Multiple failed password attempts

Privilege indicators:

* sudo activity
* root session openings

---

## MITRE ATT&CK Mapping

Mapped techniques:

* T1595 — Active Scanning
* T1046 — Network Service Discovery
* T1110 — Brute Force
* T1078 — Valid Accounts
* T1595.003 — Web Vulnerability Scanning

---

## Detection Opportunities

Potential detection rules:

* Alert on multiple failed SSH logins
* Alert on invalid users attempting authentication
* Alert on Nmap user-agent detection
* Alert on Gobuster user-agent detection
* Alert on unusual HTTP methods
* Alert on repeated 404 bursts
* Alert on sudo activity after login

---

## Recommendations

Security improvements:

* Implement Fail2Ban
* Restrict SSH exposure
* Disable root login
* Enforce strong password policies
* Limit Apache sensitive endpoints
* Apply web application firewall rules
* Monitor suspicious HTTP methods
* Improve centralized logging

---

## Lessons Learned

Honestly, during this project I learned a lot and experienced firsthand the step-by-step evolution of how an attack develops.

From the reconnaissance phase to active attack phases, I was able to understand how vulnerabilities can be discovered and how attackers usually focus on exposed services.

I learned the importance of either closing unnecessary services or implementing proper defensive rules to protect them.

I also understood how easy it can be for a single weak rule or small oversight to go unnoticed and become an entry point.

This project reinforced the importance of protocols, service hardening, and log visibility.

Thanks to the Cisco Junior Cybersecurity course, I have been learning a lot alongside this process, and this lab allowed me to apply that knowledge in a practical way.

I realized that cybersecurity is a branch of computer engineering that will never stop growing in demand and professional opportunities.

And most importantly, I realized that regardless of limitations, I want to keep learning and improving in this field.

---

## Final Reflection

This lab represents the beginning of my transition into cybersecurity.

It strengthened my understanding of:

* SOC operations
* Blue team methodology
* Incident analysis
* Log investigation
* Threat detection
* Basic detection engineering

This is only the beginning.
