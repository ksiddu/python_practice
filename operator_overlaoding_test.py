# polymorphism
# duck type: like inheritance
# operator overloading
# method overloading
# method overriding
# operator overloading for user defined class
class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        result1 = self.m1 + self.m2
        result2 = other.m1 + other.m2
        if result1 > result2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)

s1 = Student(35, 45)
s2 = Student(65, 51)

s3 = s1 + s2

print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")


print(s3)