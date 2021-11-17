class A:
    x =10
    y = 50

    def m1(self):
        print("m1 - a")

    def m2(self):
        print("m2--a")

a = A()
print(a.x)
print(a.y)
a.m1()
a.m2()

class B:
    x = 50
    z = 30

    def m2(self):
        print("m2--B")

    def m3(self):
        print("m3--B")

b = B()
print(b.x)
print(b.z)
b.m2()
b.m3()

class C(B,A):
    y = 25
    p = 52

    def m4(self):
        print("m4 --c")

    def m5(self):
        print("m5--c")

c = C()
print(c.y)
print(c.p)
c.m4()
c.m1()
c.m1()
print(c.x)
print(c.z)
c.m2()
print(b.x)


class D(C):
    a = 53
    b = 60

    def m6(self):
        print("m6--D")
    def m7(self):
        print("m7 of D")
d = D()
print(d.a)
print(d.y)
print(d.y)
print(d.p)
print(d.z)
print(d.x)
d.m6()

class E(D):
    t =60
    v = 57

    def m1(self):
        super().m2()
        print("m1 --E")

    def m8(self):
        print("m1--E")


e = E()
print(e.t)
print(e.v)
print(e.x)
print(e.y)
print(e.p)
























