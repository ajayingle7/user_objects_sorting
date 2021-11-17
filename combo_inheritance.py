class A:
    x = 10
    y = 20

    def m1(self):
        print("m1--A")

    def m2(self):
        print("m2--A")

class B:
    p = 23
    q = 33

    def m3(self):
        print("m3--B")

    def m4(self):
        print("m4--B")

class C(A,B):
    a=11
    z =14

    def m5(self):
        print("m5--C")

    def m6(self):
        print("m6--C")



class D(C):
    w= 34
    r= 44

    def m7(self):
        print("m7--D")

    def m8(self):
        print("m8--D")


class E(D):
    r=22
    k=31
    def m9(self):
        print("m9--E")

    def m10(self):
        print("m10--E")


class F(E):
    g=12
    f=54

    def m12(self):
        print("m12--F")

    def m10(self):
        print("m10--F")

class G(E):
    e=44
    h=54

    def m12(self):
        print("m12--G")

    def m8(self):

        print("m8--G")


class H(F,E):
    r =33
    n=76

    def m15(self):
        print("m15--H")

    def m16(self):
        print("m16--H")

class I(H):
    b = 32
    m = 54

    def m17(self):
        print("m17--I")

    def m18(self):
        print("m18--I")

class J(H):
    o = 65
    v=44

    def m18(self):
        print("m18--J")

    def m19(self):
        print("m19--J")


j=J()
