'''try:
    a = [10,20,30]
    print(a[10])

except IndexError as msg:
    print(msg)'''
'''
try:
    x = int('CJC')

except ValueError as msg:
    print(msg)
'''
'''try:
    x = int(["CJC"])

except Exception as msg:
    print(msg)'''

'''
try:
    print(s)

except Exception as msg:
    print(msg)'''

'''
try:
    Counter = 0

    def m1():
        Counter+=1

    m1()
except Exception as msg:
    print(msg)'''

'''
def m1():
    b = 20
    try:
        a = 10/0
        print("In try")
        return 10

    except:

        print("In except")
        return b

x = m1()
print(x)'''

'''def m2():
    a = 5

    try:
        a = 10/0
        print("In try")
        return a

    except:
        print("In except")
        return a

x = m2()
print(x)'''

'''
def m3():
    a =5

    try:
        a = 10
        print("In try")
        b = 10/0
        return a

    finally:
        print("In finally")
        return a

x = m3()
print(x)'''

'''def m4():
    a = 5

    try:
        a = 10
        print("In try")
        b = 10/0
        return a

    finally:
        a = 30
        print("In finally ",a)
        return 30

b = m4()
print(b)'''


def m5():
    try:
        a = 10
        print("In try")
        b = 10 / 0
        return a

    finally:
        print("In finally", a)
        return 30
        return 40


z = m5()
print(z)






























































































