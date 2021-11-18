class A:
    def __init__(self):
        self.name = "Ajay"
        print(self.name)

    def show1(self):

        name = "vijay"
        print(name)
class B(A):
    def show2(self,middlename):
        print(middlename)

class C(A):
    def __init__(self):
        super(C).__init__()


        self.surename = "Ingle"

    def show3(self):
        print(self.surename)
obj1 = B()
obj1.show1()