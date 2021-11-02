class Myclass:
    name = "Ajay"
    email = "ajayingle109@gmail.com"
    mno = 7770078554


    def f1(self,name,email):
        return name,email

    def f2(self):
        self.f1("vijay","vijay@gmail.com")

    def __str__(self):
        return f"{self.name},{self.email},{self.mno}"

obj2 = Myclass()
print(obj2)
print(obj2.f1("vijay","ajay@gmail.com"))