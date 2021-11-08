# empty set

set1 = set()
print(type(set1))

#set example

set2 = {1,2,3,4,5,6,"Ajay",2.5,True}
print(set2)

# set methods

set3 = {1,2,3,4,5,6,7}
print(set3.pop())

print(set3.remove(5))

print(set3.add(100))

set4 = print(set3.copy())
print(set4)

print(set3.clear())


# set union, intersection , difference

myset1 = {1,2,3,4,5,6}
myset2 = {1,2,3,4,5,5,6,7,8}
print(myset1.union(myset2))

print(myset1.intersection(myset2))

print(myset1.difference(myset2))

#iteration
for i in myset1:
    print(i)









