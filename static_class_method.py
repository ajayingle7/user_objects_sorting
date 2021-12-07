class A:

    name = "Ajay"


    def m11(self):
        print("instance method")

    @staticmethod
    def m():
        print("static mathod 1")


    @staticmethod
    def m1(x):
        A.m()
        print(x)

    @classmethod
    def m2(cls):
        cls.m1(123)
        print(cls.name)



A.m1("SAchin")

obj1= A()

obj1.m2()