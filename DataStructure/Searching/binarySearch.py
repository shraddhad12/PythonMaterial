def binarySearch(array, value):
    start = 0
    end = len(array)
    mid = (start+end)//2

    while not(array[mid] == value) and start<=end:
        if value < array[mid]:
            end = mid - 1
        else:
            start = mid + 1 
        mid = (start+end)//2

    if array[mid] == value:
        return 1
    else:
        return -1
    
print(binarySearch([1,2,3,4,5,6,7], 6))
