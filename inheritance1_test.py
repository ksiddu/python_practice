class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

# multi level inheritance
class C(B):
    def feature5(self):
        print("Feature 5 working")


a1 = A()

a1.feature1()
a1.feature2()

# class B has access to both methods of A & B using inheritance
b1 = B()

b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

# class C has access to both methods of A , B  & C using inheritance
c1 = C()

c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()