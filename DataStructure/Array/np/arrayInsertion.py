import numpy as np

array = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,7],[4,5,6,7]])

new_array1 = np.insert(array, 1, [[2,2,2,2]], axis=0) # 0 is row and 1 is for column ## adding at index
print(new_array1) 

new_array2 = np.append(array, [[2,2,2,2]], axis=0) ## adding at last and taking less time
print(new_array2)