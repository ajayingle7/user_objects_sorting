class A:
    def __init__(self,a):
        print(a)


class B(A):
    def __init__(self,a):
        print(a)
        super().__init__(10)

obj1 = B(20)