import subprocess
# only linux

class ServiceMonitor:
    def __init__(self, service_name):
        self.service_name = service_name

    def check_status(self):
        """Check the current status of the service."""
        status = subprocess.getoutput(f"systemctl is-active {self.service_name}")
        return status

    def restart_service(self):
        """Restart the service if it's not active."""
        status = self.check_status()
        if status != "active":
            print(f"{self.service_name} is not running. Restarting...")
            subprocess.run(["systemctl", "restart", self.service_name], check=True)
        else:
            print(f"{self.service_name} is running.")

# Example Usage
monitor = ServiceMonitor("gnome")
monitor.restart_service()
