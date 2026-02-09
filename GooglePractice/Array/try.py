import numpy as np
matrix = np.array([
    [1,2,3,4],
    [2,3,4,5],
    [3,4,5,5],
    [4,5,6,7]
])                ## complexity O(N)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print( matrix[i][j] , end = "")
#     print()
# print(matrix)
# for row in matrix:
#     # print(" ".join(map(str, row)))
#     print(row)

[print(" ".join(map(str, row))) for row in matrix]


import array
matrix = array.array('i', [4,5,6,7]) ## complexity O(N)
print(matrix)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print( matrix[i][j] , end = "")
#     print()