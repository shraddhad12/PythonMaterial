def rotate(d, arr):
    return arr[d:]+arr[:d]

arr = [10, 45, 80, 95, 70]
print(f"Array before rotating", arr)
d= 2
rotate_list = rotate(d, arr)
print(f"Array before rotating from index {d}", rotate_list)