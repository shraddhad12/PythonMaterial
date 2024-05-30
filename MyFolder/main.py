import functools

def validate_integers(func):
    @functools.wraps(func)
    def wrapper(*args):
        if not all(isinstance(arg, int) for arg in args):
            raise ValueError("All arguments must be integers")
        return func(*args)
    return wrapper

@validate_integers
def sum(a, b):
    return a+b

print(sum(3, 3))


class A:
    def sum(self):
        print("class A sum")

class B:
    def sum(self):
        print("class B sum")

class C(A, B):
    pass

class D(C, B):
    pass

d =D()
d.sum()

for i in range(5):
    if i%2:
        print(i)
else:
    print(i) 