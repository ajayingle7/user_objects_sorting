
class Myclass:

    def setname(self,name):
        self.__name = name

    def setroll(self,roll):
        self.__roll = roll

    def getname(self):
        return self.__name

    def getroll(self):
        return self.__roll

    def _m1(self):
        print("m1___A")


obj1 = Myclass()
obj1.setname("AJay")
obj1.setroll(23)

print(obj1.getname())
print(obj1.getroll())
obj1._m1()