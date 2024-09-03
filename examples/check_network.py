import os
import time

# List of hosts to ping
hosts = ["8.8.8.8", "google.com", "192.168.1.1"]

# Log file to store ping results
logfile = "network_check.log"

def check_connectivity():
    with open(logfile, "a") as f:
        for host in hosts:
            response = os.system(f"ping -c 1 {host} > /dev/null 2>&1")
            status = "reachable" if response == 0 else "unreachable"
            log_entry = f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {host} is {status}\n"
            f.write(log_entry)
            print(log_entry, end="")

while True:
    check_connectivity()
    time.sleep(60)  # Check every 60 seconds
