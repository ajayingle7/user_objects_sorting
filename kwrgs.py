def myfun(**data):
    print(data)

myfun(name = "Ajay", surename = "Ingle", City = "Pune")


class A:
    def fun(self,**info):
        for i in info.values():
            print(i)

a = A()
a.fun(name = "Ajay",surename = "Ingle", city= "Kaij", mno = 7770078554)