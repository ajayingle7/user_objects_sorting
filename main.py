class Student:
    def __init__(self,roll,name):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"{self.roll}{self.name}"

num = int(input("enter objects: "))

list1= []
for i in range(num):
    obj1 = Student(int(input("roll")),input("name"))
    list1.append(obj1)

list1.sort(key=lambda x: x.name)

for j in list1:
    print(j)