import sys


# Function to detect sudo and privilege-related activity
def analyze_sudo_activity(log_path):
    try:
        sudo_count = 0
        root_session_count = 0

        print("\n[+] Privilege-related activity detected:\n")

        with open(log_path, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:

                # Detect sudo command execution
                if "sudo:" in line:
                    sudo_count += 1
                    print("[SUDO ACTIVITY] " + line.strip())

                # Detect root session activity
                elif "session opened for user root" in line:
                    root_session_count += 1
                    print("[ROOT SESSION] " + line.strip())

        print("\n[+] Summary:")
        print(f"Sudo events: {sudo_count}")
        print(f"Root session events: {root_session_count}")

        if sudo_count == 0 and root_session_count == 0:
            print("No privilege-related activity found.")

    except FileNotFoundError:
        print(f"[!] File not found: {log_path}")

    except PermissionError:
        print(f"[!] Permission denied: {log_path}")


# Script entry point
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python sudo_activity_parser.py <auth.log>")
        sys.exit(1)

    analyze_sudo_activity(sys.argv[1])