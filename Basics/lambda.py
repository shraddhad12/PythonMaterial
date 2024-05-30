fun = lambda x, y: x+y
print(fun(5, 6))

from functools import reduce
print(reduce(lambda x, y: x if x > y else y, [47,12,42,102,13])) #to find max and min


list1 = [2,3,2,4,5,6,7,6,6]

even =lambda list1: list(i for i in list1 if i%2 == 0)
for i in even(list1):
    print(i)

result = reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) #find sum
print(result)