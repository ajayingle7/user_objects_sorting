def square():
    for i in range(1, 11):
        yield i * i


obj1 = square()
for i in obj1:
    print(i)


def cube():
    num = int(input("enter range: "))

    for i in range(num):
        yield i * i * i


obj2 = cube()
for j in obj2:
    print(j)


def rest():
    n = "A"
    yield n

    n = "J"
    yield n
    n = "A"
    yield n

    n = "Y"
    yield n


obj3 = rest()
for i in obj3:
    print(i)


def m1():
    string = "WHERE ARE YOU NOW"

    for i in string[::-1]:
        yield i


obj5 = m1()

for i in obj5:
    print(i)


def even1():
    for i in range(1, 11):
        if (i % 2 == 0):
            yield i


for i in even1():
    print(i)


def str1(str):
    for i in str[::-1]:
        yield i


obj10 = str1("full stack deve")
for i in obj10:
    print(i)

import math


def circle():
    area = 10
    for i in range(area):
        yield "area of ", i, math.pi * i * i


obj12 = circle()

for i in obj12:
    print(i)







































