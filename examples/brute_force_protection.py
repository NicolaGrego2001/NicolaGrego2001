import os
import re
import subprocess
import time

# Log file to monitor
logfile = "/var/log/auth.log"

# IPs to block
blocked_ips = set()

# Regex pattern to match failed SSH login attempts
pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

def block_ip(ip):
    if ip not in blocked_ips:
        os.system(f"iptables -A INPUT -s {ip} -j DROP")
        blocked_ips.add(ip)
        print(f"Blocked IP: {ip}")

with open(logfile, "r") as f:
    f.seek(0, 2)  # Move to the end of the file

    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue

        match = pattern.search(line)
        if match:
            block_ip(match.group(1))
