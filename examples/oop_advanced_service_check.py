import subprocess
import logging
import platform
import win32serviceutil  # pip install pywin32
from abc import ABC, abstractmethod

# Set up logging
logging.basicConfig(filename='service_monitor.log', level=logging.INFO, format='%(asctime)s - %(message)s')


class Service(ABC):
    """Abstract base class representing a system service."""

    def __init__(self, service_name):
        self.service_name = service_name

    @abstractmethod
    def check_status(self):
        """Check the current status of the service."""
        pass

    @abstractmethod
    def restart_service(self):
        """Restart the service."""
        pass


class LinuxService(Service):
    """Concrete class for handling services on Linux using systemctl."""

    def check_status(self):
        """Check the current status of the service."""
        status = subprocess.getoutput(f"systemctl is-active {self.service_name}")
        return status

    def restart_service(self):
        """Restart the service if it's not active."""
        status = self.check_status()
        if status != "active":
            logging.info(f"Linux service {self.service_name} is not running. Restarting...")
            subprocess.run(["systemctl", "restart", self.service_name], check=True)
        else:
            logging.info(f"Linux service {self.service_name} is running.")


class WindowsService(Service):
    """Concrete class for handling services on Windows using pywin32."""

    def check_status(self):
        """Check the current status of the service."""
        try:
            status = win32serviceutil.QueryServiceStatus(self.service_name)[1]
            if status == 4:  # 4 represents the 'running' state
                return "active"
            else:
                return "inactive"
        except Exception as e:
            logging.error(f"Error checking status of Windows service {self.service_name}: {e}")
            return "unknown"

    def restart_service(self):
        """Restart the service if it's not active."""
        status = self.check_status()
        if status != "active":
            logging.info(f"Windows service {self.service_name} is not running. Restarting...")
            try:
                win32serviceutil.RestartService(self.service_name)
                logging.info(f"Windows service {self.service_name} restarted.")
            except Exception as e:
                logging.error(f"Error restarting Windows service {self.service_name}: {e}")
        else:
            logging.info(f"Windows service {self.service_name} is running.")


class ServiceMonitor:
    """Class to monitor multiple services on Linux and Windows."""

    def __init__(self, services):
        self.services = services

    def monitor_services(self):
        """Monitor all services and restart them if necessary."""
        for service in self.services:
            service.restart_service()


# Detect the operating system and choose the correct service class
def create_service(service_name):
    """Factory method to create a service based on the current operating system."""
    if platform.system() == "Linux":
        return LinuxService(service_name)
    elif platform.system() == "Windows":
        return WindowsService(service_name)
    else:
        raise OSError("Unsupported operating system")


# Example Usage
if __name__ == "__main__":
    services_to_monitor = ["nginx", "mysql"] if platform.system() == "Linux" else ["Spooler",
                                                                                   "wuauserv"]  # Example services

    services = [create_service(service_name) for service_name in services_to_monitor]

    monitor = ServiceMonitor(services)
    monitor.monitor_services()
