def deco(fun):
    def inn(a,b):
        if b==0:
            raise ZeroDivisionError("cant divide by zero")

        else:
            print(a/b)

    return inn

def deco2(fun):
    def inn(*num):
        total = fun(*num)
        final_amt = total/2
        return final_amt
    return inn




@deco                             #decorator
def m1(a,b):
    print(a/b)

m1(10,12)



@deco2
def m2(*num):
    sum =0
    for i in num:
        sum+=i

    return sum

print("total is: ", m2(10,20,50,852))
