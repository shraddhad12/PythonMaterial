print("=========================Bubble Sort=================================")

def bubbleSort(arr): 
    for i in range(1, len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [5,7,8,1,9,4,3]
print("Before Sort",arr)
print("Using Bubble Sort",bubbleSort(arr))