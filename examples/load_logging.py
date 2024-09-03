import psutil
import time

# Service name to monitor
service_name = "/usr/share/pycharm/jbr//bin/java"

# Log file to store resource usage data
logfile = "service_resource_usage.log"

with open(logfile, "a") as f:
    while True:
        # Get the process ID (PID) of the service
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == service_name:
                pid = proc.info['pid']
                p = psutil.Process(pid)

                # Log CPU and memory usage
                log_entry = f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}, CPU: {p.cpu_percent()}%, Memory: {p.memory_percent()}%\n"
                f.write(log_entry)
                print(log_entry, end="")

        time.sleep(10)  # Log every 10 seconds
