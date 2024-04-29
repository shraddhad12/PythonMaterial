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

print("========================Insertion Sort==================================")

def insertionSort(arr): 
    for i in range(len(arr)-1):
        temp = i
        sorted_arr = i+1
        while sorted_arr > 0:
            if arr[sorted_arr] < arr[temp]:
                arr[sorted_arr], arr[temp] = arr[temp], arr[sorted_arr]
            sorted_arr -= 1
            temp -= 1

    return arr
arr = [5,7,8,1,9,4,3]
print("Before Sort",arr)
print("Using Insertion Sort",insertionSort(arr))

print("=======================Merge Sort===================================")

# def merge(arr, l, m, r): 

#     n1 = l+m
#     n2 = r-m

#     print("n1", n1)
#     print("n1", n2)

#     L1 = [0] * n1
#     L2 = [0] * n2
#     for i in range(0, n1-1):        
#         L1[i] = arr[l+i]
    
#     for j in range(0, n2):
#         L2[j] = arr[m+j]
#     print(L1)
#     print(L2)

# def mergeSort(arr, l , r):
#     if l < r:
#         m = (l+(r-1))//2
#         print("length", len(arr))
#         print("mid", m)
#         mergeSort(arr, l, m)
#         mergeSort(arr, m+1, r)
#         merge(arr, l, m ,r)
#         return arr

arr = [5,7,8,1,9,4]
print("Before Sort",arr)
# print(mergeSort(arr, 0, len(arr)))