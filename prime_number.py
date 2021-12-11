'''fh = open("text1.txt",'r')

while True:
    line = fh.readlines()
    print(line)
    if not line:
        break

fh.close()


fh = open("text1.txt")
data = fh.read()
data = data.split()

print(data)

for line in data:
    x = int(input("enter a line number: "))

    print(data[x])

fh.close()

fh = open("text1.txt","r")
data = fh.read()

occure = data.count('h')
print(occure)
fh.close()



fh = open('text1.txt')
data = fh.read()
fh.close()

x = data.replace('monday','MONDAY')
fh = open('text1.txt','w')
fh.write(x)
fh.close()'''



fh = open("text1.txt",'r')

a=  fh.readlines()

if len(a)>8:
    print(a)

print(a)



















