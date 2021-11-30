'''def m1():

    try:

        a = 10/0
        print("in try")
        return 10

    except:
        print("in except")
        return 20

x = m1()
print(x)


def m1():
    a = 5

    try:
        a=10
        b = 10/0
        print("in try")
        return a

    except:
        print("in except")
        return a

x = m1()
print(x)



def f1():
    a = 5
    try:
        a = 10
        print("try--block")
        b = 10/0
        print(b)
        return a


    except ZeroDivisionError:
        print("enter non zero value")



    finally:
        print("in finally")










def m1():
    a  =10

    try:
        a=5
        print("try --block ")
        b = 10/0
        return a


    except Exception:
        print("enter non zero values ")
    finally:
        a = 30
        print("in finally",a)
        return a
x = m1()
print(x)




def m1():

    try:
        a = 10
        print("in--try")
        b = 10/0

    finally:
        print("in finally",a)

        return 30
        return 40

x = m1()
print(x)


print("program start")

try:

    a = 10/2

    try:
        print("inner try")
        b = [1,2,3]
        print(b[2])
        print("inner try end")

    except IndexError:
        print("inner except block")

except ZeroDivisionError:
    print("outer except block")

print("program end")

print("program start")

try:

    print("outer try start")
    a = 10/2
    print("outer try end")

    try:
        print("inner try start")
        b = [1,2,3]
        print(b[1])
        print("inner try end")

    except IndexError:
        print("index error")

except:
    print("outter except block")

print("program end")




try:
    print("program --start")
    a = 10/2

    try:
        print("inner try start")
        b = [1,2,3]
        print(b[10])
        print("inner try end")

    except Exception as msg:
        print("inner except block",msg)

except ZeroDivisionError:
    print("outer except block")

finally:
    print("in finally")
    print("porgram end")


print("program start")

try:
    print("try start")
    a = 10/0
    print("try end")

except ZeroDivisionError:
    print("in except block")

    try:

        print("except try start")
        b = [1,2,3]
        print(b[2])
        print("except try end")

    except IndexError:
        print("except except block")

finally:
    print("in finally")


print("program start")

try:

    print("outer try start")
    a = 10/2

    try:
        print("inner try start")
        b = [1,2,3]
        print(b[10])
        print("inner try end")

    finally:

        print("inner finally")

except:
    print("outer except block")

finally:
    print("outer finally ")

print("program end")
'''

























































































