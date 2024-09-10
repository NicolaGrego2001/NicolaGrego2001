from abc import ABC, abstractmethod

class Computer(ABC):
    cpu: int
    ram: int
    disk: int

    def __init__(self, cpu: int, ram: int, disk: int):
        self.cpu = cpu
        self.ram = ram
        self.disk = disk

    @abstractmethod
    def power_on(self):
        ...


class Dell(Computer):
    def power_on(self):
        print(f"Premo bottone in alto a destra")

class Mac(Computer):
    def power_on(self):
        print(f"Premo bottone in alto a sinistra")