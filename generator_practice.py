def generator():

    print("generator start of odd: ")

    for i in range(1,11,2):
        yield i

    print("generator start of even: ")

    for j in range(0,11,2):
        yield j

    print("end of generator")

for i in generator():
    print(i)



def generator2():

    for i in range(1,11,1):
        for j in range(1,11,1):
            yield i ,'*',j ,'=',i*j


for i in generator2():
    print(i)