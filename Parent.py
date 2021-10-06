class Parent:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("Parent a value ", a)
        print("Parent b value ", b)


    def sum(self):
        return self.a + self.b


#obj = Parent(5, 10)
#result = obj.sum()
#print(result)