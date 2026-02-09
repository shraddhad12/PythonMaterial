def shiftZerosLeft(arr):
    left = len(arr) -1
    right = len(arr) -1

    while right >= 0 :
        if arr[right] != 0:
            arr[right] , arr[left] = arr[left], arr[right]
            left -= 1
        right -= 1

    return arr

def shiftZerosRight(arr):
    left = 0
    right = 0

    while right < len(arr) :
        if arr[right] != 0:
            arr[right] , arr[left] = arr[left], arr[right]
            left += 1
        right += 1

    return arr

arr = [2,4,0,4,0,5,0,0]
print(shiftZerosLeft(arr))
print(shiftZerosRight(arr))