'''def deco(fun):
    def inner(*prices):
        total  = fun(*prices)
        discount = total*0.3
        total_amt = total-discount

        return total_amt
    return inner



@deco
def bill(*prices):

    sum = 0

    for i in prices:
        sum+=i
    return sum

print("total bill is: ", bill(100,55,255))'''

def decorato(fun):
    def inner(name):
        print("hii",name)

    return inner




@decorato
def m1(name):
    print("hello",name)

print(m1("ajay"))







def deco(fun):
    def inner(msg):
        if len(msg)>=10:
            print(msg)

        else:
            print("limit is above 10")
    return inner

@deco
def m1(msg):
    if len(msg)<=10:
        print(msg)

    else:
        print("length exceeded")

m1('ajsdfghhgfdfghjmhgfddfg')

































