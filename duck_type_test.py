# polymorphism
# duck type: like inheritance
# operator overloading
# method overloading
# method overriding


class MyEditor:
    def execute(self):
        print("Spell check")
        print("Syntax check")
        print("Compiling")
        print("Executing")

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Executing")

class Laptop:
    def __init__(self, ide):
        ide.execute()

ide1 = PyCharm()
l1 = Laptop(ide1)

ide2 = MyEditor()
l1 = Laptop(ide2)