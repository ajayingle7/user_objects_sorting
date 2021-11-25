class Myclass:

    def setname(self,name):
        self.__name = name

    def setroll(self,roll):
        self.__roll = roll

    def getname(self):
        return self.__name

    def getroll(self):
        return self.__roll

obj1 = Myclass()
obj1.setname("AJay")
obj1.setroll(23)

print(obj1.getname())
print(obj1.getroll())
print(dir(obj1))