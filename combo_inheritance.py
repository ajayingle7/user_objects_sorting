class Product1:
    def __init__(self,name):
        self.name = name
    def m1(self):
        print(self.name)

class Product2:
    def __init__(self,middlename):
        self.middlename = middlename

    def m2(self):
        print(self.middlename)

class Product3(Product1,Product2):
    def __init__(self,Surename):
        self.surename = Surename

    def m3(self):
        print(self.surename)

class Product4(Product3):
    def __init__(self,Sister):
        self.sister = Sister

    def m4(self):
        print(self.sister)

class Product5(Product4):
    def __init__(self,Brother):
        self.brother = Brother

    def m4(self):
        print(self.brother)

class Product6(Product5):
    def __init__(self,Niece):
        self.niece = Niece

    def m5(self):
        print(self.niece)

class Product7(Product5):
    def __init__(self,grand_mother="sangita"):
        self.grand_mother = grand_mother

    def m6(self):
        print(self.grand_mother)


class Product8(Product7,Product6):
    def __init__(self,grand_father):
        self.grand_father = grand_father

    def m7(self):
        print(self.grand_father)



p = Product8('bankat')
p.m7()
print(p.grand_mother)

