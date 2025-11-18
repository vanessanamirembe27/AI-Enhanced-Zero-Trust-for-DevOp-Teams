import subprocess
import sys
import time
from colorama import Fore, Style, init

# Initialize color output
init(autoreset=True)

def run_pipeline():
    print(Fore.CYAN + "\nStarting CI/CD Pipeline Simulation...\n")
    stages = [
        "Checkout Source Code",
        "Build Application",
        "Run Zero Trust Policy Check",
        "Deploy to Production"
    ]
    
    for stage in stages:
        print(Fore.MAGENTA + f"Stage: {stage}")
        time.sleep(1.2)
        
        # Run Zero Trust check during security validation stage
        if stage == "Run Zero Trust Policy Check":
            print(Fore.YELLOW + "Running Zero Trust validation script...")
            time.sleep(1)
            result = subprocess.run(
                ["python", "zero_trust_check.py"],
                capture_output=True,
                text=True
            )
            
            # Detect blocked communications in output
            if "blocked" in result.stdout.lower():
                print(Fore.RED + "\nPolicy violation detected — deployment stopped.\n")
                print(Fore.WHITE + "Zero Trust Check Output:")
                print(Fore.LIGHTBLACK_EX + result.stdout)
                print(Fore.YELLOW + "\nReview and update communication policies before retrying.\n")
                sys.exit(1)
            else:
                print(Fore.GREEN + "\nPolicy check passed — safe to deploy.\n")
                
        elif stage == "Deploy to Production":
            print(Fore.GREEN + "Deployment successful. Application live.\n")
    
    print(Fore.MAGENTA + "Pipeline completed.\n")

if __name__ == "__main__":
    run_pipeline()