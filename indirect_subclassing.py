from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class B:
    def m1(self):
        print("m1--B")

A.register(B)

print(issubclass(B,A))
