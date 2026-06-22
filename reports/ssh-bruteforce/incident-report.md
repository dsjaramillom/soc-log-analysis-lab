# Incident Report — SSH Authentication Analysis

## 1. Summary

This lab simulates and analyzes SSH authentication activity on an Ubuntu Server. The objective is to identify failed login attempts, distinguish invalid user attempts from legitimate access, and document the investigation process as a SOC Tier 1 analyst.

## 2. Environment

* Target machine: Ubuntu Server
* Attacker machine: Kali Linux
* Service analyzed: SSH
* Log source: `/var/log/auth.log`
* Network type: VirtualBox lab network

## 3. Log Preparation

Before generating the test events, the authentication log was cleared to isolate the activity related to this lab.

Command used:

```bash
sudo truncate -s 0 /var/log/auth.log
```

## 4. Observed Events

The authentication log showed the following relevant events:

### Failed SSH Attempt

An invalid user attempted to authenticate through SSH.

```text
Failed password for invalid user david from 192.168.56.11
```

This indicates a login attempt using a non-existent account.

### Successful SSH Login

A valid login was observed for the legitimate user.

```text
Accepted password for analyst from 192.168.56.11
```

This confirms successful authentication using a valid account.

### Privileged Activity

After login, the user executed commands with elevated privileges.

```text
session opened for user root by analyst
```

This indicates that the authenticated user used `sudo`.

## 5. Analysis

The failed login attempt suggests possible SSH probing, user enumeration, or the beginning of a brute-force attempt. The successful login was expected and used as a baseline for comparison.

Key observations:

* Invalid user attempted: `david`
* Valid user observed: `analyst`
* Source IP: `192.168.56.11`
* Target service: SSH
* Authentication result: both failed and successful events observed

## 6. MITRE ATT&CK Mapping

* T1110 — Brute Force
* T1078 — Valid Accounts

## 7. Recommendations

* Disable SSH password authentication and use SSH keys.
* Restrict SSH access by trusted IP addresses.
* Enable Fail2Ban to block repeated failed attempts.
* Monitor `/var/log/auth.log` for repeated authentication failures.
* Alert on invalid user attempts and multiple failed logins from the same IP.

## 8. Conclusion

This lab demonstrates basic SSH authentication log analysis. The investigation identified failed authentication attempts, successful access, and privileged activity using Linux authentication logs.
