
# def merge(left, right):
#     i, j = 0,0
#     new = []

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             new.append(left[i])
#             i += 1
#         else:
#             new.append(right[j])
#             j += 1

#     new.extend(left[i:])
#     new.extend(right[j:])
#     return new
    

# def mergeSorting(customList):
#     if len(customList) <= 1:
#         return customList

#     mid = len(customList)//2
#     l_half = customList[:mid]
#     r_half = customList[mid:]
#     l_half = mergeSorting(l_half)
#     r_half = mergeSorting(r_half)

#     return merge(l_half, r_half)

def merge(left, right):
    i, j = 0, 0
    new = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new.extend(left[i:])
    new.extend(right[j:])
    return new

def mergeSorting(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    l_half = arr[:mid]
    r_half = arr[mid:]

    l_half = mergeSorting(l_half)
    r_half = mergeSorting(r_half)
    return merge(l_half, r_half)


arr = [2,4,6,1,3,8,9,0, 5]
print(mergeSorting(arr))
    