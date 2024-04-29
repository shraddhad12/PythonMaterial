print("=======================Selection Sort==================================")

def selectionSort(arr):
    for i in range(len(arr)-1):
        temp = i
        for j in range(i+1, len(arr)):
            if arr[temp] > arr[j]:
                temp = j
        arr[i], arr[temp] = arr[temp], arr[i]
    return arr
arr = [5,7,8,1,9,4,3]
print("Before Sort",arr)
print("Using Selection Sort", selectionSort(arr))