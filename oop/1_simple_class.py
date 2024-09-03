class Computer:
    def __init__(self, name, ram, hdd):
        self.name = name
        self.ram = ram
        self.hdd = hdd

    def turn_on(self):
        print(f"{self.name} is turning on")

    def turn_off(self):
        print(f"{self.name} is turning off")

    def free_mem(self) -> int:
        return 10

my_computer = Computer(name='Dell', ram=16, hdd=512)

print(my_computer.hdd)
my_computer.turn_on()
print(my_computer.free_mem())
my_computer.turn_off()