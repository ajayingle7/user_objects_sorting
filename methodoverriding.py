class A:
    def show(self):
        print("parent class")

class B:
    def show1(self):

        print("b class")
class C(A,B):
    def show(self):
        print("c class")


obj1 = A()
obj1.show()

obj2 = C()
obj2.show()

