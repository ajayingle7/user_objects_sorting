class A:
    def myfun(self,*args):
        for i in args:
            print(i)


b = A()
b.myfun("ajay","vijay","sanjay")
