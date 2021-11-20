class A:
    def __init__(self,x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __mul__(self, other):
        return self.x * other.x

    def __sub__(self, other):
        return self.x - other.x


obj1 = A(10)
obj2 = A(20)
obj3 = A(30)

print(obj1+obj2)
print(A(obj1+obj2)+obj3)    # addition

print(obj1*obj2)

