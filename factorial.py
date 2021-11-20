num = int(input("enter a number: "))

fact = 1

if num<0:
    print("negetive number has not factorial")

elif num==0:
    print("factorial of 0 is 1")

else:
    for i in range(1,num+1):
        fact= fact*i

    print("factrial of ", num, "is",fact)
