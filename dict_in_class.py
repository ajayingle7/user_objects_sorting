class Employee:

    def __init__(self,emp_name,emp_sal,emp_mno):
        self.name = emp_name
        self.sal = emp_sal
        self.mno = emp_mno

    def __str__(self):
        dict1 = {}
        dict1.update({1:self.name,2:self.sal,3:self.mno})
        return f"{dict1}"

objects = int(input("enter objects: "))

list1 = []

for i in range(objects):
    name = input("enter name: ")
    sal = int(input("enter a sal: "))
    mno = int(input("enter a mno: "))

    obj1 = Employee(name,sal,mno)

    list1.append(obj1)

for i in list1:
    print(i)

