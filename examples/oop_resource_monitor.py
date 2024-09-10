import psutil

class ResourceMonitor:
    def __init__(self):
        pass

    def get_cpu_usage(self):
        """Return the current CPU usage."""
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self):
        """Return the current memory usage."""
        mem_info = psutil.virtual_memory()
        return mem_info.percent

    def monitor(self):
        """Monitor and display resource usage."""
        cpu_usage = self.get_cpu_usage()
        memory_usage = self.get_memory_usage()
        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")

# Example Usage
monitor = ResourceMonitor()
monitor.monitor()
