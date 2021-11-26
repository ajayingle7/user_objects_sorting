class Student():
    _name = "Ajay"


    def _m1(self):
        print("m1-- Student")
        return self._name

    def m2(self):
        return self._name

    def __str__(self):
        return f"{self._name}"


class Display(Student):
    def m1(self):
        super()._m1()
        print(super().m2())
        print(self._name)

obj1 = Display()
obj1.m1()
print(obj1)