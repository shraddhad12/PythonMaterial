a = (1,2, [1,2])
a[2][0] = 2
print(a)
###List inside the tuple can changed the elements


x = 257 #"hello"
y = 257 #"hello"
print(x==y)
print(x is y)


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)  # Output: False, because a and b are different objects in memory
print(a is c)  # Output: True, because a and c are the same object in memory