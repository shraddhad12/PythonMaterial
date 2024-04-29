import numpy as np


arr1 = np.array([[4, 7, 5, 7, 8, 5]] )
arr2 = np.array([[3, 6, 0, 0, 0, 0]]) 
print(arr1)
print(arr2)

print(np.add(arr1, arr2))

print(np.sum(arr1))

print(np.sqrt(arr1))

print("transpose", arr1.T)

print(np.append(arr1, arr2))

print(np.sort(arr1))

metrix = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print(metrix[:2]) #2 rows desplayed
print(metrix[:1, :2]) #1 row, 2 cloums

if 4 in arr1:
    print(f"4 is present in {arr1}")

print(arr1[::-1])

for i in arr1:
    print(i)