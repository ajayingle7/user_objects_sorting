'''def myfun(a=0,b=0):

    if a!=0 and b!=0:
        print(a,b)
        print(b)

    elif a!=0:
        print(a)

    else:
        print("no parameter")

myfun(10,20)
myfun(45)
myfun()
'''


def m1(*args):
    print(*args)

m1(2,11,222,45,6,2,5,6,3,4,6,7,4,77)