def myfun():

    print("this is function starting")

    yield 100

    print("this is miidle of yield")

    yield 200

    print("end of function")


a = myfun()


for i in a:
    print(i)



class A:

    def even(self):
        print("fun starting")
        name = "Saurabh"
        yield 100

        for i in range(10,20):
            yield i


        for i in range(1,51):
            if i%2==0:
                yield i

        yield name

        print("end of fun")
obj1 = A()
obj2 = obj1.even()
print(next(obj2))

































