from operator import attrgetter
class A:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"



s1 = A("vijay",21)
s2 = A("Ajay",20)

list1 = [s1,s2]
list1.sort(key=lambda a:a.name)
for i in list1:
    print(i)

print(dir(s1))