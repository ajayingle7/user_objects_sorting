class A:
    def __init__(self,name,city):
        self.name=name
        self.city =city

    def __str__(self):
        return f"{self.name},{self.city}"


obj=int(input("enter your object: "))

list1= []

for i in range(obj):
    name = input("enter a name")
    city = input("enter a city")

    s1 = A(name,city)
    list1.append(s1)

for j in list1:
    print(j)