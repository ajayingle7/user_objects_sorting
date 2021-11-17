class A:
    def __init__(self):
        self.name = "Ajay"


class B:

    def __init__(self):
        self.middlename = "sanjay"


class C(B, A):

    def __init__(self):
        self.surename = "Ingle"

    def display(self):
        print(self.name, self.middlename, self.surename)


obj1 = C()
obj1.display()


