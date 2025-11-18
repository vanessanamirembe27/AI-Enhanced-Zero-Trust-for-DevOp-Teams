from __future__ import print_function
import csv
import os
import sys
from colorama import Fore, init
from zero_trust_check import simulate_communications

# Prepare color support
init(autoreset=True)

LOG_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "continuous_logs.csv")

def count_blocked(log_path):
    if not os.path.exists(log_path):
        print(Fore.YELLOW + "No log file found at " + log_path)
        return 0

    blocked = 0
    with open(log_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("action", "") == "blocked":
                blocked += 1
    return blocked

def main():
    print(Fore.CYAN + "Running Zero Trust gate check...")

    # Run simulation before evaluating
    simulate_communications()

    blocked = count_blocked(LOG_FILE)
    print(Fore.CYAN + f"Detected {blocked} blocked communications.")

    if blocked > 0:
        print(Fore.RED + "Zero Trust Gate FAILED — Violations detected.")
        sys.exit(1)
    else:
        print(Fore.GREEN + "Zero Trust Gate PASSED — No violations.")
        sys.exit(0)

if __name__ == "__main__":
    main()