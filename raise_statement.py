class MyError(Exception):
    def __init__(self,msg):
        self.msg  =msg


class TimeError(Exception):
    def __init__(self,msg):
        self.msg = msg






try:
    a = int(input("enter a no"))

    if a>10:
        raise MyError("value is above 10")

    elif a<1:
        raise TimeError("value is below 1")

    else:
        print(a)

except MyError as msg:
    print(msg)

except TimeError as msg:
    print(msg)