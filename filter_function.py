def filterdata(x):
    if x>5:
        return x

result = filter(filterdata,(1,2,6))
print((list(result)))


result2 = filter(filterdata,(2,6,8,14,0,25,4,3))
print(list(result2))

list1 = [10,20,30,40,50]
result3 = list(filter(lambda x:x>10,list1))
print(result3)


