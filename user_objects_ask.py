class Dog():
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name},{self.color}"

list1 = []

obj = int(input("enter how many object you want: "))

for i in range(obj):
    name = input("enter a name: ")
    color = input("enter a color: ")

    obj1 = Dog(name,color)

    list1.append(obj1)

for i in list1:
    print(i)