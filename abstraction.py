from abc import ABC,abstractmethod

class Absclass(ABC):

    @abstractmethod
    def m1(self):
        print("m1--Abstract")

    @abstractmethod
    def m2(self):
        print("m2--Abstract")

    @abstractmethod
    def m3(self):
        print("m3--Abstract")

    def m4(self,name):
        print("name : ", name)




class child(Absclass):

    def m1(self):
        print("m1--child")

    def m2(self):
        print("m2--child")

    def m4(self,surename):
        print("surenamnme", surename)



obj = child()
obj.m4("ingle")
obj.m1()
