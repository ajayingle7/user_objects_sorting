class AgeInvalidError(Exception):
    def __init__(self, message):
        self.msg = message


class MnoError(Exception):
    def __init__(self, msg):
        self.msg = msg


def f1(age, mno):
    print("f1--start")

    if age > 65:
        raise AgeInvalidError("age is above 65")

    elif len(mno) > 10:
        raise MnoError("mno is invalid")


try:
    f1(63, "7770078554111")

except Exception as a:
    print(a)

