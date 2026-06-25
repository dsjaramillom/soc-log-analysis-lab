import sys


# Function to analyze failed SSH login attempts
def analyze_failed_logins(log_path):
    try:
        # Open the log file in read mode
        # encoding/errors helps avoid crashes with strange characters
        with open(log_path, "r", encoding="utf-8", errors="ignore") as file:

            # Counter for failed login attempts
            failed_count = 0

            print("\n[+] Failed SSH login attempts detected:\n")

            # Read file line by line
            for line in file:

                # Look for lines containing "Failed password"
                if "Failed password" in line:
                    failed_count += 1

                    # Print the suspicious log entry
                    print(line.strip())

            # Show total number of failed attempts
            print(f"\n[+] Total failed login attempts: {failed_count}")

    # Handle file not found error
    except FileNotFoundError:
        print(f"[!] File not found: {log_path}")

    # Handle permission issues
    except PermissionError:
        print(f"[!] Permission denied: {log_path}")


# Entry point of the script
if __name__ == "__main__":

    # Validate that the user provides the log file path
    if len(sys.argv) != 2:
        print("Usage: python failed_logins.py <auth.log>")
        sys.exit(1)

    # Run the analysis function using the provided file path
    analyze_failed_logins(sys.argv[1])