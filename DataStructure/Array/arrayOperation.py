import array 

# Create an array
matrix = array.array('i', [1,2,3,4,5])

## Insert an element at 0th index
matrix.insert(0, 6)


## Insert an element at 3th index
matrix.insert(3, 3)

## delete last element
matrix.pop()

## delete element
matrix.pop(3)

## delete element
matrix.remove(6)

print(matrix)


# traverse an array
for i in matrix:
    print(i, end=" ")

print()
print()

#Access Element
print(matrix[len(matrix)-1])   # ==================== O(1)
print()
print()
index = 1
print(matrix[index])