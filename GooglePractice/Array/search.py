def binary_search(arr, number):
    left = 0
    right = len(arr)
    mid = (left+right)//2
    while not(arr[mid] == number) and left <= right:
        if arr[mid] > number:
            right = mid - 1
        else: 
            left = mid + 1
        mid = (left+right)//2
    if arr[mid] == number:
        return mid
    return -1

print("Number is found at index", binary_search([1,2,3,4,5], 1))