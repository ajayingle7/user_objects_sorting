class A:
    x = 10

    def m1(self):
        print("class a fun")

class B(A):

    def f2(self):
        print("class b fun")
        print(self.x)
        self.m1()

b = B()
b.f2()




class X:
        def __init__(self):
            print("class a constructor")

class Y(X):
        def __init__(self):
            print("class b constructor")
            super().__init__()

x= Y()



