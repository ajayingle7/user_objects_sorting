'''counter = {}
def addtocounter(country):
    if country in counter:
        counter[country]+=1

    else:
        counter[country] = 1

addtocounter("japan")
addtocounter("china")
addtocounter("india")

print(len(counter))


a = "hello world"
b = 12
print(a+b)

dictionary = {}
dictionary[1] = 1
dictionary['1'] = 2
dictionary[1] += 1
print(dictionary)

sum = 0
for k in dictionary:
    sum += dictionary[k]

print(sum)



namelist = ["Harsh","Kevin","Bob","Dhruv"]
print(namelist[1][-1])



codes = [1,2,3,4]
codes.append([5,6,7,8])
print(len(codes))


check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
check3 = check1[:]

check2[0] = 'Code'
check3[1] = 'Mcq'

count = 0
for c in (check1, check2, check3):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'Mcq':
        count += 10

print(count)

def f1(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


f1(2)
f1(3, [3, 2, 1])
f1(3)


list1 = ['a', 'b', 'c'] * 3
print(list1)

dictionary1 = {'Google' : 1,
               'Facebook' : 2,
               'Microsoft' : 3
               }
dictionary2 = {'Chrome' : 1,
               'Microsoft' : 2,
               'Youtube' : 3
               }
dictionary1.update(dictionary2)
for key, values in dictionary1.items():
    print(key, values)



temp = dict()
temp['key1'] = {'key1' : 44, 'key2' : 566}
temp['key2'] = [1, 2, 3, 4]
for (key, values) in temp.items():
    print(values, end = "")


data = [2, 3, 9]
temp = [[x for x in[data]] for x in range(3)]
print (temp)



data = [x for x in range(5)]
temp = [x for x in range(7) if x in data and x%2==0]
print(temp)

L1 = list()
L1.append([1, [2, 3], 4])
L1.extend([7, 8, 9])
print(L1[0][1][1] + L1[2])


temp = ['Please', 'pay', 'Tax']
arr = [i[0].upper() for i in temp]
print(arr)

L1 = [1, 1.33, 'CJC', 0, 'NO', None, 'C', True]
val1, val2 = 0, ''
for x in L1:
    if(type(x) == int or type(x) == float):
        val1 += x
    elif(type(x) == str):
        val2 += x
    else:
        break
print(val1, val2)


t1 = (1)
t2 = (3,4)
t1+=5
print(t1+t2) #error




List = [True, 50, 10]
List.insert(2, 5)
print(List, "Sum is: ", sum(List))



T = (1, 2, 3, 4, 5, 6, 7, 8)
print(T[T.index(5)], end = " ")

print(T[T[T[6]-3]-6])


fruits = ["a","b","c"]

fruits.copy(1)
print(fruits)


i =0
while i<10:
    i+=1
    print(i)


L = [1, 3, 5, 7, 9]
print(L.pop(-3), end = '  ')
print(L.remove(L[0]), end = '  ')
print(L)


L= [1,3,5,7,9]
print(L.pop(-3),  end = ' ' )
print(L.remove(L[0]),end=' ')
print(L)


def m1(L):
    L.reverse()
    return L

def m2(L):
    list1 = list()
    list1.extend(m1(L))
    print(list1)


L = [1,3.1,5.3,7.531]
m2(L)


D = {1 : 1, 2 : '2', '1' : 1, '2' : 3}
D['1'] = 2
print(D[D[D[str(D[1])]]])'''




















































































































































































































































