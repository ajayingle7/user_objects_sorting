class Samsung_Global:
    def Brand(self,model):
        return model

    def Price(self,price):
        return price

class Samsung_India(Samsung_Global):

    def Brand(self,model):
        return model

    def Price(self,price):
        return price

class Samsung_USA(Samsung_Global):
    def Brand(self,model):

        print(Samsung_Global.Price(self,150000))
        print(Samsung_Global.Brand(self,"global"))
        return model

    def Price(self,price):
        return price


obj1 = Samsung_USA()
obj1.Price(11500)
print(obj1.Brand("Note 9 Pro USA"))
