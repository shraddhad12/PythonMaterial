import numpy as np

metrix = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

for i in range(len(metrix)):
    for j in range(len(metrix[0])):
        print(int(metrix[i][j]))
