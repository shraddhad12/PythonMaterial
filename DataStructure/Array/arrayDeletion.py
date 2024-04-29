import numpy as np

metrix = np.array([[-1, 2, 0, 4],
                [4, -5, 6, 0],
                [6, 0, 7, 8],
                [3, -7, 4, 2]])
new_array = np.delete(metrix, 1, axis=1) #Removed column
print(new_array)

new_array = np.delete(metrix, 1, axis=0) #Removed Row
print(new_array)