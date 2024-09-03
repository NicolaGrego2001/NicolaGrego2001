import psutil
import time

# Log file to store bandwidth usage data
logfile = "network_bandwidth.log"

with open(logfile, "a") as f:
    while True:
        net_io = psutil.net_io_counters()
        log_entry = f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}\n"
        f.write(log_entry)
        print(log_entry, end="")
        time.sleep(5)  # Monitor every 5 seconds