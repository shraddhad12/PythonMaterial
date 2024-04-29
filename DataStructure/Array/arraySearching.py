import numpy as np

def search(metrix, value):
    for i in range(len(metrix)):
        for j in range(len(metrix[0])):
            if metrix[i][j] == value:
                return f"The value {value} is located at index {i}, {j}"
            else:
                continue
    return f"The value {value} is not present in given metrix"


metrix = np.array([[-1, 2, 0, 4],
                [4, -5, 6, 0],
                [6, 0, 7, 8],
                [3, -7, 4, 2]])
print(search(metrix, -7))


