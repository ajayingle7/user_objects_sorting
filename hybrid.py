class A:
    def __init__(self,a,b):
        self.a = "a __init__"
    def m1(self):
        print("class of A")

class B(A):
    def __init__(self):
        self.b = "b __init__"
    def m2(self):
        print("class of B")

class C(A):
    def __init__(self):
        super().__init__()
        self.c = "c __init__"
    def m3(self):
        print("class of C")

class D(B,C):
    def __init__(self):
        print("d __init__")
    def m4(self):
        super().__init__()
        print("class of D")

obj = D()
obj.m4()




