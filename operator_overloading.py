class A:
    def __init__(self,x):
        self.x = x


    def __add__(self, other):
        return self.x + other.x
    def __eq__(self,other):
        return self.x == other.x
    def __truediv__(self, other):
        return self.x / other.x

obj1 = A(10)
obj2 = A(20)

print(obj1+obj2)

print(obj1==obj2)

print(obj2/obj1)