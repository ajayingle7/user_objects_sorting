print("hello world")


def m1():
    a = int(input("enter number: "))

    b = int(input("enter number:"))
    try:
        print("hey brother")
        print(a / b)
        print("hello guys")

    except ZeroDivisionError as msg:
        print("except--block", msg)


m1()


