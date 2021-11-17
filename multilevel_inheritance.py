class A:
    def __init__(self):
        self.name = "ajay"

    def f1(self):
        print(self.name)

class B(A):

    def __init__(self):
        super().__init__()
        self.surename = "ingle"

    def f2(self):
        print(self.surename)

class C(B):

    def __init__(self):
        super().__init__()
        self.middlename = "Sanjay"
    def f3(self):
        self.f1()
        print(self.name,self.middlename,self.surename)



obj = C()
obj.f3()
obj.f1()
obj.f2()

print(C.__mro__)




