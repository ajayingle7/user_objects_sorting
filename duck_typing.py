class A:
    def f1(self):
        print("f1--A")

    def f2(self):
        print("f2--A")


class B:
    def f1(self):
        print("f1--B")

    def f2(self):
        print("f2--B")

def myfun(para):
    para.f1()
    para.f2()

myfun(B())
myfun(A())

