def factorial(n):
    return 1 if (n==0 or n==1) else n * factorial(n-1)

num = 5
print(f"factorial of {num} is", factorial(num))