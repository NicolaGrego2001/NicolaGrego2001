import requests

# File to store the last known IP address
ip_file = "/var/log/last_known_ip.txt"

# Get the current public IP address
current_ip = requests.get("https://api.ipify.org").text

# Check if the IP has changed
try:
    with open(ip_file, "r") as file:
        last_ip = file.read().strip()

    if current_ip != last_ip:
        print(f"IP address has changed: {last_ip} -> {current_ip}")
        with open(ip_file, "w") as file:
            file.write(current_ip)
    else:
        print(f"IP address is unchanged: {current_ip}")
except FileNotFoundError:
    # Save the current IP for the first time
    with open(ip_file, "w") as file:
        file.write(current_ip)
    print(f"Initial IP address recorded: {current_ip}")
