

class A:
    def __init__(self,a,b):
        self.start = a
        self.end = b

    def __iter__(self):
        return self

    def __next__(self):

        if self.end <self.start:
            raise  StopIteration("exceeded")
        else:
            n = self.start
            self.start += 2
            return n

obj1 = A(10,50)
obj2 = obj1.__iter__()
for i in obj2:
    print(i)




class B:

    def __init__(self,a):
        self.initial = a

    def __iter__(self):
        return self

    def __next__(self):
        self.limit = 100

        if self.limit< self.initial:
            raise StopIteration("exceed")

        else:

            n = self.initial
            self.initial +=2
            return n

obj1 = B(100)
obj2 = obj1.__iter__()
for i in obj2:
    print(i)



























