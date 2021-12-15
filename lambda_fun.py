'''print((lambda *names:names)("ajay","vijay","sanjay","patil"))

print((lambda **info:info)(name = "Ajay",age= 22,city = "Pune"))'''




age = [5,11,18,23,25,67,90]

#filter
adults = list(filter(lambda x:x>18,age))
print(adults)

#map
increase_age = list(map(lambda x:x+10,age))
print(increase_age)

#reduce
from functools import reduce

age = [11,2,3,4,5,6,7]

add_age = reduce((lambda x,y:x+y),age)
print(add_age)

