import psutil

# CPU usage threshold (in percentage)
cpu_threshold = 80.0

# Check all processes
for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
    try:
        if proc.info['cpu_percent'] > cpu_threshold:
            print(f"Killing process {proc.info['name']} (PID: {proc.info['pid']})")
            psutil.Process(proc.info['pid']).terminate()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass