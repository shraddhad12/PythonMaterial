def return_fun():
    for i in range(10):
        return i
    
def yield_fun():
    for i in range(10):
        yield i
    
print(return_fun()) # Output: 0
print(yield_fun()) # Output: <generator object yield_fun at 0x7f0b1f2e0d60>

for i in yield_fun():
    print(i)