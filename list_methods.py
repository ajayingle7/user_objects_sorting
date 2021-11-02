list1 = [2,5,6,7,8,1,9]
list2 = [11,12,13]
list1.sort()
print(list1)

print(list1.append(10))
print(list1)

print(list1.extend(list2))
print(list1)

list1.copy()
a = list1.copy()
print(a)

list1.pop(9)
print(list1)

print(list1.count(13))

print(list1.index(13))

print(list1.reverse())
print(list1)

list1.remove(11)
print(list1)




