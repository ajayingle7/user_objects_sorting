def m1():


    print("m1--start")

    print(10/0)
    print("m1--end")


try:          #giving change to caller handle the exception is called exception propogetting
    m1()

except ZeroDivisionError as msg:
    print(msg,"error")