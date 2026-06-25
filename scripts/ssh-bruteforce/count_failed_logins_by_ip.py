import sys
import re
from collections import Counter


# Function to extract source IPs from failed SSH login attempts
def count_failed_logins_by_ip(log_path):
    try:
        # Counter stores each IP and how many times it appears
        ip_counter = Counter()

        # Open the authentication log file
        with open(log_path, "r", encoding="utf-8", errors="ignore") as file:

            # Read the log file line by line
            for line in file:

                # Only analyze failed SSH login attempts
                if "Failed password" in line:

                    # Extract the IP address after the word "from"
                    match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

                    # If an IP address is found, add it to the counter
                    if match:
                        source_ip = match.group(1)
                        ip_counter[source_ip] += 1

        print("\n[+] Failed SSH login attempts by source IP:\n")

        # Print results sorted from highest to lowest count
        for ip, count in ip_counter.most_common():
            print(f"{ip} -> {count} failed attempts")

        # If no failed attempts were found
        if not ip_counter:
            print("No failed SSH login attempts found.")

    except FileNotFoundError:
        print(f"[!] File not found: {log_path}")

    except PermissionError:
        print(f"[!] Permission denied: {log_path}")


# Entry point of the script
if __name__ == "__main__":

    # Validate argument count
    if len(sys.argv) != 2:
        print("Usage: python count_failed_logins_by_ip.py <auth.log>")
        sys.exit(1)

    # Run analysis
    count_failed_logins_by_ip(sys.argv[1])