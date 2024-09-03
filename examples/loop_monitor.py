import psutil
import time

# Log file to store the monitoring data
logfile = "resource_monitor.log"

with open(logfile, "a") as f:
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent

        log_entry = f"CPU: {cpu_usage}%, Memory: {memory_usage}%\n"
        f.write(log_entry)
        print(log_entry, end="")

        time.sleep(5)  # Monitor every 5 seconds
