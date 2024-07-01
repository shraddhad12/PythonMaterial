# # a = set([1, 2, 3, 3])
# # a.add(4)

# a = {1,2,3,4,{2,3}}
# print(a)

# Sample list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
even_numbers_list = list(even_numbers)
print(even_numbers_list)  # Output: [2, 4, 6, 8, 10]
print("Even numbers:", even_numbers)


class A:

    def __init__(self):
        self.a = 12

    def method1(self):
        print("instace method")


    # @classmethod
    # def method2(self):
    #     print("class method")

    # @staticmethod
    # def method3():
    #     print("static method")
        
class B:
    def __init__(self, obj):
        self.obj = obj

    # def __new__(self):
    #     return A()

    def result(self):
        print(self.obj.a)

a = A()
b = B(a)
b.result()


from datetime import datetime
import time
def dec_fun(fun):
    def wrapper(x, y):
        start_time = time.time()
        print(time.time())
        result = fun(x,y)
        print("execution time ", time.time() - start_time)
        print(time.time())
        return result
    return wrapper

@dec_fun
def sum(x,y):
    print(x)
    print(y)
    print(x+y)
    return x + y

print(sum(1,2))

a = [1,0,0,1,0,1]
a.sort()
print(a)

