# Check if given array is Monotonic
# Monotonic means if the array is in increasing or descrasing order
def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    print(x, y)
    if(x == A or y == A):
        return True
    return False


# Driver program
A = [6, 5, 4, 4]
B = [2,5,7,2]
C = [2,5,7,9]

# Print required result
print(f"{A} is Monotonic - ", isMonotonic(A))
print(f"{B} is Monotonic - ", isMonotonic(B))
print(f"{C} is Monotonic - ", isMonotonic(C))