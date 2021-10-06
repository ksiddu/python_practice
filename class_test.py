
class Computer:

    def __init__(self, cpu, ram, memory):
        self.cpu = cpu
        self.ram = ram
        self.memory = memory


    def config(self):
        print("Pentium, 5 GB, 1 TB")

    def config2(self):
        print("Config is ", self.cpu, self.ram, self.memory)



# 1st way of calling class method
#comp1 = Computer()
#comp1.config()


# 2nd way of calling class method
#comp2 = Computer()
#Computer.config(comp2)

#print(type(comp1))
#print(type(comp2))

#print(__name__)

# 1st way of calling class method
comp3 = Computer('i5', '5 Gb', '1 TB')
comp3.config2()

comp4 = Computer('i6', '6 Gb', '2 TB')
comp4.config2()

# 2nd way of calling class method
comp5 = Computer('i7', '7 Gb', '3TB')
Computer.config2(comp5)