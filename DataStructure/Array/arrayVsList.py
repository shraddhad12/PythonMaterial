import numpy as np



#Can not perform arithmetic operations on list directly

myList = [1, 3, 6, 8, 4]
myArray = np.array([1, 3, 6, 8, 4])

print(myArray/2)
# print(myList/2) # will raise error - unsupported operand type(s) for /: 'list' and 'int'

#list accepts different type of data
#Array doesn't accept different type of data

myList = [1, 3, 6, 8, 4, 'a']
myArray = np.array([1, 3, 6, 8, 4, 'a']) #convert all the values to string
print(myList)
print(myArray)