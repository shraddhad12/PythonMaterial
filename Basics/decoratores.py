def adv_add(fun):
    def inner(a,b):
        return fun(a, b)
    return inner

def add(x, y):
    return x + y

add = adv_add(add)
print(add(5, 6))

# def dec(fun):
#     print("this is addintion method")
#     fun()

# @dec
# def sum(x, y):
# 	print(x+y)

# dec(sum(5, 6))

import functools

def validate_integers(func):
    @functools.wraps(func)
    def wrapper(*args):
        if not all(isinstance(arg, int) for arg in args):
            raise ValueError("All arguments must be integers")
        return func(*args)
    return wrapper

@validate_integers
def sum2(a, b):
    return a+b
print(sum2(3, 3))



def validate_integers(func):
    def wrapper(x, y):
        if not isinstance(x, int) and not isinstance(y, int):
            raise ValueError("All arguments must be integers")
        return func(x, y)
    return wrapper

def sum3(a, b):
    return a+b

sum3 = validate_integers(sum3)
print(sum3(3, 3))



def validate_integers2(func):
    def wrapper(x, y):
        if not isinstance(x, int) and not isinstance(y, int):
            raise ValueError("All arguments must be integers")
        return func(x, y)
    return wrapper

@validate_integers2
def sum3(a, b):
    return a+b

print(sum3(3, 3))




	
	
