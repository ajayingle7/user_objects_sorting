print("hello world")


def m1():
    a = int(input("enter number: "))

    b = int(input("enter number:"))
    try:
        print("hey brother")
        print(a / b)

        a = open("return.py","r")


        print("hello guys")
        b = [1,2]
        print(b[1])



    except (ZeroDivisionError,IOError,SyntaxError,NameError,AttributeError,IndexError) as msg:
        print("except--block", msg)

    finally:
        print("helloooo")
        def m2():
            a = 10
            b = 20
            print(a+b)
        m2()


m1()


