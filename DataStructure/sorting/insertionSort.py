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