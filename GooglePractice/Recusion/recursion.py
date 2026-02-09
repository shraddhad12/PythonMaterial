def factorial(n):
    if not n:
        return 1
    return n * factorial(n-1)

def fibonacii(n):
    if n ==0 or n == 1:
        return n
    return fibonacii(n-1) + fibonacii (n-2)

def insidesubset(i, lists, new):
    if i == len(lists):
        print(new)
        return
    new.append(i)
    insidesubset(i+1, lists, new)
    new.pop()
    insidesubset(i+1, lists, new)
      
def subset(arr):
    i = 0
    new = []
    insidesubset(i, arr, new)


print("factorial of 4 is : ", factorial(4))
print("fibonacci term at 8th position is : ", fibonacii(8))
subset([1,2,3])

