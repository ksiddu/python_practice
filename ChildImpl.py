from Parent import Parent


class Child(Parent):
    def __init__(self, a, b):
        super().__init__(a, b)
        print("Child a value ", a)
        print("Child b value ", b)


childObj = Child(3, 4)
result = childObj.sum()
print(result)
