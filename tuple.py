a = input("enter a number: ")

b = tuple(a)

count = 0

for i in b:
    print('tuple',count,i)
    count= count+1