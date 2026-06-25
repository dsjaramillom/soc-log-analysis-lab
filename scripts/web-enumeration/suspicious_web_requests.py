import sys


# Suspicious HTTP methods often linked to reconnaissance
SUSPICIOUS_METHODS = ["OPTIONS", "PROPFIND", "POST"]

# Sensitive or interesting paths
SUSPICIOUS_PATHS = ["/server-status", "/.htaccess", "/.htpasswd", "/.hta"]


# Function to analyze suspicious web requests
def analyze_web_requests(log_path):
    try:
        print("\n[+] Suspicious web requests detected:\n")

        with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
            suspicious_count = 0

            for line in file:

                # Detect known attacker user-agents
                if "gobuster" in line.lower() or "nmap" in line.lower():
                    suspicious_count += 1
                    print("[USER-AGENT MATCH] " + line.strip())
                    continue

                # Detect suspicious HTTP methods
                for method in SUSPICIOUS_METHODS:
                    if f'"{method} ' in line:
                        suspicious_count += 1
                        print("[METHOD MATCH] " + line.strip())
                        break

                # Detect sensitive paths
                for path in SUSPICIOUS_PATHS:
                    if path in line:
                        suspicious_count += 1
                        print("[PATH MATCH] " + line.strip())
                        break

        print(f"\n[+] Total suspicious web events: {suspicious_count}")

    except FileNotFoundError:
        print(f"[!] File not found: {log_path}")

    except PermissionError:
        print(f"[!] Permission denied: {log_path}")


# Script entry point
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python suspicious_web_requests.py <access.log>")
        sys.exit(1)

    analyze_web_requests(sys.argv[1])