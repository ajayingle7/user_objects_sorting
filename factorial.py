num  = int(input("enter a numberL:"))

fact = 1

if num<0:
    print("negetive value dont have a factorial")

elif num==0:
    print(0)

else:

    for i in range(1,num+1):
        fact = fact*i

    print(fact)