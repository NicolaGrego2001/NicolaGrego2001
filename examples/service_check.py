import os
import subprocess

# Service name
service_name = 'nginx'

# Check service status
status = subprocess.getoutput(f"systemctl is-active {service_name}")

# Restart the service if it's not running
if status != 'active':
    os.system(f"systemctl restart {service_name}")
    print(f"{service_name} service restarted.")
else:
    print(f"{service_name} service is running.")
