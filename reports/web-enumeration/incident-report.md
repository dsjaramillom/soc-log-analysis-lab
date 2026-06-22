# Incident Report — Web Enumeration Analysis

## Summary

This lab simulates web directory enumeration against the Ubuntu Apache server using Gobuster.

The objective was to discover hidden paths and analyze how enumeration activity appears in Apache logs.

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
gobuster dir -u http://192.168.56.10 -w /usr/share/wordlists/dirb/common.txt
```

Purpose:

* Directory discovery
* Hidden endpoint detection
* Web surface enumeration

---

## Findings

### Discovered Paths

```text
/.hta
/.htpasswd
/.htaccess
/index.html
/server-status
```

---

## Response Codes

### 200 OK

```text
/index.html
```

Accessible content.

---

### 403 Forbidden

```text
/.hta
/.htpasswd
/.htaccess
/server-status
```

Protected resources exist.

This confirms restricted internal endpoints.

---

## Log Evidence

Apache logs showed repeated enumeration attempts.

Observed patterns:

```text
GET /you
GET /z
GET /zap
GET /yii
GET /xml
```

User-Agent:

```text
gobuster/3.8.2
```

This confirms active directory brute forcing.

---

## Indicators of Compromise (IoCs)

Source IP:

```text
192.168.56.11
```

User-Agent:

```text
gobuster/3.8.2
```

Pattern:

High volume sequential HTTP GET requests.

---

## MITRE ATT&CK Mapping

* T1595.003 — Web Vulnerability Scanning

---

## Impact

Enumeration revealed:

* Existing protected files
* Default index page
* Restricted server status endpoint

This information could support further attack planning.

---

## Recommendations

* Restrict access to sensitive endpoints
* Disable unnecessary directory indexing
* Implement WAF rules
* Detect high-frequency sequential requests
* Monitor Gobuster signatures in logs

---

## Evidence

Screenshots:

* `screenshots/web-enumeration/01-gobuster-scan.png`
* `screenshots/web-enumeration/02-apache-log-impact.png`

Raw logs:

* `logs/web-enumeration/gobuster-results.txt`
