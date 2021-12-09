class My_class:

    def __init__(self,start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        self.limit = 20

        if self.limit<self.start:
            raise StopIteration

        else:
            n = self.start
            self.start+=2
            return n

obj1 = My_class(10)

obj2= obj1.__iter__()




















