# c = [1,2,3]
# d=c
# c[0]=100
# print(d[0])

# a=10
# b=a
# a=5
# print(b)


# select id, max(salary < max(salary))
# from user


l = [[0,23,43], [3,4,5],[3,5,7],[7,8,9],[0,23,43], [3,4,5], [0,45], [345], [0]]

list1 = [lambda x: x[0] != 0, l]
for i in list(list1):
    print(i)