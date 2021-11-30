def m1(mno):

    print("m1--start")
    if len(mno)>10:
        raise KeyError("enter 10 digits only")
    elif len(mno)<10:
        raise KeyError("enter 10 digits")

try:
    mno = input("enter a mno: ")
    m1(mno)

except Exception as msg:
    print(msg)
