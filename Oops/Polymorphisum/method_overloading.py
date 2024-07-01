'''
In many object-oriented programming languages, method overloading allows multiple methods in the same class to have the same name but different parameters. 
However, Python does not support method overloading in the traditional sense. In Python, you cannot define multiple methods with the same name 
but different signatures in the same class. Instead, Python supports method overriding and offers alternative ways to achieve similar functionality to method overloading.
'''

#Using default Argument
class MyClass:
    def display(self, a, b=0):
        if b == 0:
            print(f"One argument: {a}")
        else:
            print(f"Two arguments: {a} and {b}")
obj = MyClass()
obj.display(10)       # Output: One argument: 10
obj.display(10, 20)   # Output: Two arguments: 10 and 20

#Using default Argument
class MyClass:
    def display(self, a):
        print(f"One argument: {a}")

    def display(self, a, b):
        print(f"Two arguments: {a} and {b}")
obj = MyClass()
obj.display(10)      
obj.display(10, 20)   




# Using *args - Variable Lenth ARGUMENT
class MyClass:
    def display(self, *args):
        if len(args) == 1:
            print(f"One argument: {args[0]}")
        elif len(args) == 2:
            print(f"Two arguments: {args[0]} and {args[1]}")
        else:
            print("Invalid number of arguments")
obj = MyClass()
obj.display(10)       # Output: One argument: 10
obj.display(10, 20)   # Output: Two arguments: 10 and 20
obj.display(10, 20, 30)  # Output: Invalid number of arguments



# using *args and **kwargs Together -
'''
 This approach can handle both positional and 
 keyword arguments, providing even more flexibility.
'''
class MyClass:
    def display(self, *args, **kwargs):
        if 'name' in kwargs:
            print(f"Name: {kwargs['name']}")
        print(f"Arguments: {args}")
obj = MyClass()
obj.display(10, 20, name="John")  # Output: Name: John
                                  #          Arguments: (10, 20)



