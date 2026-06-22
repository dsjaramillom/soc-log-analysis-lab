# Incident Report — Nmap Reconnaissance Analysis

## Summary

This lab simulates a reconnaissance phase using Nmap against the Ubuntu target server.

The objective was to identify exposed services, enumerate versions, and observe how reconnaissance activity appears in system and web logs.

---

## Source Information

Source IP:

```text
192.168.56.11
```

Attacker machine:

* Kali Linux

Target IP:

```text
192.168.56.10
```

Target machine:

* Ubuntu Server

---

## Command Used

```bash
nmap -A 192.168.56.10
```

Purpose:

* Service detection
* Version enumeration
* OS fingerprinting
* NSE script execution
* Attack surface mapping

---

## Findings

### Open Ports

```text
22/tcp open ssh
80/tcp open http
```

---

### Service Enumeration

#### SSH

```text
OpenSSH 10.2p1 Ubuntu
```

Risk:

Exposed SSH service may be targeted for brute force or credential attacks.

---

#### Apache

```text
Apache httpd 2.4.66
```

Risk:

Web service exposed and available for further enumeration.

---

### Operating System Detection

```text
Linux
```

This confirms successful fingerprinting of the target.

---

## Log Evidence

Apache logs showed multiple reconnaissance-related requests.

Observed requests:

```text
GET /
OPTIONS /
PROPFIND /
POST /sdk
GET /HNAP1
GET /evox/about
GET /favicon.ico
```

User-Agent detected:

```text
Nmap Scripting Engine
```

Analysis:

This confirms active HTTP service fingerprinting and endpoint probing.

---

## Indicators of Compromise (IoCs)

Source IP:

```text
192.168.56.11
```

User-Agent:

```text
Nmap Scripting Engine
```

Suspicious paths:

* /HNAP1
* /sdk
* /evox/about

---

## MITRE ATT&CK Mapping

* T1595 — Active Scanning
* T1046 — Network Service Discovery

---

## Impact

Reconnaissance revealed:

* Open services
* Service versions
* Operating system
* Web server capabilities

This information could be used for future attack planning.

---

## Recommendations

* Restrict unnecessary service exposure
* Monitor Nmap signatures in logs
* Implement rate limiting
* Harden exposed services
* Use a web application firewall (WAF)
* Alert on unusual HTTP methods like PROPFIND or OPTIONS

---

## Evidence

Screenshots:

* `screenshots/nmap-recon/01-nmap-scan-results.png`
* `screenshots/nmap-recon/02-apache-log-impact.png`

Raw logs:

* `logs/nmap-recon/nmap-scan.txt`
