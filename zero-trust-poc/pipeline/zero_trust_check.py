import json
import csv
import time
import datetime
from colorama import Fore, Style, init

# Initialize colorama for terminal color output
init(autoreset=True)

# Load policy from JSON
with open('../policies/network-policy.json', 'r') as f:
    policy = json.load(f)

services = policy["services"]

#CSV log file path
log_file = "../data/continuous_logs.csv"

#Double checking for headers
try:
    with open(log_file, 'r') as f:
        pass
except IOError:
    with open(log_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "source", "destination", "action", "reason"])

def log_event(source, dest, action, reason):
    """Append event to continuous CSV log file."""
    with open(log_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            source,
            dest,
            action,
            reason
        ])

def check_communication(source, destination):
    """Check if source can communicate with destination based on policy."""
    allowed_list = services.get(source, {}).get("allowed", [])
    
    if destination in allowed_list:
        print(Fore.GREEN + source + " → " + destination + " : Communication allowed")
        log_event(source, destination, "allowed", "explicit policy rule")
    else:
        print(Fore.RED + source + " → " + destination + " : Communication blocked (policy violation)")
        log_event(source, destination, "blocked", "not in allowed list")

def simulate_communications():
    """Simulate communication attempts between all services."""
    for source in services.keys():
        for dest in services.keys():
            if source != dest:
                check_communication(source, dest)

if __name__ == "__main__":
    simulate_communications()