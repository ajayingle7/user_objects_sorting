class A:
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name}, {self.email}"

obj = A("ajay","ajayingle109@gmail.com")
obj2 = A("vijay","vjijay@gmail.com")

tuple1 = (obj,obj2)

for i in tuple1:
    print(i)