'''
Private Access Modifier
Private members are intended to be inaccessible from outside the class. This is indicated by a double underscore prefix (__). 
Python uses name mangling to make it harder (but not impossible) to access private members from outside the class.

Protected Access Modifier
Protected members are intended to be accessible only within the class and its subclasses. In Python, this is indicated by a single underscore prefix (_).

'''
'''
Benefits of Encapsulation
Control Access to Data: Encapsulation allows you to control who can access and modify the data. By providing getter and setter methods, you can add logic to control how data is accessed and modified.
Prevent Accidental Modification: By restricting access to the internal state, you prevent accidental changes that could lead to bugs or inconsistent states.
Improve Code Maintenance: Encapsulation helps in maintaining the code by separating the internal implementation from the external interface. This makes the code easier to understand, test, and refactor.
Encourage Modular Design: Encapsulation promotes modular design by ensuring that each class has a well-defined interface and its internal details are hidden from other classes.

'''

'''
Encapsulation is about bundling the data and methods and controlling access to them, 
while abstraction is about hiding complex details and exposing only the necessary parts of an object. 
'''

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self._b = "protected" 
        self.__c = "private"

    def getter(self):
        return self.__c 

# Creating a derived class
class Derived(Base):

    __d = 123  #global variable

    def __init__(self):

        # Calling constructor of
        # Base class
        self.base = Base()
        print("Calling private member of base class: ")

    def show(self):
        print("public", self.base.a)
        print("protected", self.base._b)
        # print("private", self.base.__c) #raise an AtrributeError


# Driver code
obj1 = Derived()
obj1.show()

obj2 = Base()
# print(obj2.__c) # AttributeError: 'Base' object has no attribute '__c'
print("private valiavle through the getter", obj2.getter())

print("=========================================================")


class MyClass:
    def __init__(self, value):
        self.__private_value = value

    def __private_method(self):
        return f"Private method says: {self.__private_value}"

    def public_method(self):
        return self.__private_method()

# Usage
obj = MyClass("Hello")
# print(obj.__private_value)  # AttributeError: 'MyClass' object has no attribute '__private_value'
# print(obj.__private_method())  # AttributeError: 'MyClass' object has no attribute '__private_method'

# Access through name mangling
print(obj._MyClass__private_value)  # Not recommended
print(obj._MyClass__private_method())  # Not recommended

# Access through public method
print(obj.public_method())  # Recommended way to access private method