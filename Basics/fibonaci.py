# Function for nth Fibonacci number
 
def fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        f=[]
        a, b = 1, 2
        f.append(a)
        f.append(b)
        for i in range(n-1):   
            c = a + b
            f.append(c)
            a = b
            b = c
        return f
    
# Driver Program   
print(fibonacci(9)) # Output: 0 1 1 2 3 5 8 13 21 34


def fibonaci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

print(fibonaci(100)) # Output: 0 1 1 2 3 5 8 13 21 34 55 89


            
 
