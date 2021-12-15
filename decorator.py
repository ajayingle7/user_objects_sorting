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





























