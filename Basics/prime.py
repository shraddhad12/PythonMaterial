# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

from math import sqrt

def prime_or_not(number):
    print(int(sqrt(number)))
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return "Given number is not a prime number"
    return "Given number is a prime number"
print(prime_or_not(29)) # Output: 1