
# instance methods: instance variables
# class methods: class variables
# static methods: common that doesn't deal with any variables(instance, class)
class Student:

    name = "Telusko" # class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1 # instance variable
        self.m2 = m2 # instance variable
        self.m3 = m3 # instance variable

    def avg(self): # instance method
        return (self.m1 + self.m2 + self.m3 )/3

    @classmethod
    def getSchoolName(cls): # class method
        print(cls.name)

    @staticmethod
    def info(): # static method
        print("It's as class in abc module")

s1 = Student(34, 23, 56)

s2 = Student(44, 33, 56)

print(s1.avg())

print(s2.avg())

print(Student.getSchoolName())

print(Student.info())