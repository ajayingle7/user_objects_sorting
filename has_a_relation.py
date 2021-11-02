class Cust_Info:
    def __init__(self,name,mno,city):
        self.name = name
        self.mno = mno
        self.city = city

    def __str__(self):
        return f"{self.name}, {self.mno}, {self.city}"
class Cust_Detail:
    def __init__(self,email,info):
        self.email= email
        self.info = info

    def __str__(self):
        return f"{self.email}, {self.info}"

obj1 = Cust_Info("Ajay",7770078554,"Pune")
obj2= Cust_Detail("ajayingle109@gmail.com",obj1)
print(obj2)




