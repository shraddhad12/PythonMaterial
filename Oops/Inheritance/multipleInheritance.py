'''
In multiple inheritance, a class can inherit attributes and methods from more than one superclass.
This allows for greater flexibility but can also introduce complexity, especially with the method resolution order (MRO).

When dealing with multiple inheritance, Python uses the C3 linearization algorithm to determine the method resolution order (MRO). 
The mro() method or the __mro__ attribute can be used to see the order in which classes are searched for methods and attributes.

print(MultiDerived.mro())
# Output: [<class '__main__.MultiDerived'>, <class '__main__.Derived1'>, <class '__main__.Derived2'>, <class '__main__.Base'>, <class 'object'>]
'''

class A(object):
    def __init__(self):
        super().__init__()
        print("inside super class A")

    def showA(self):
        print("inside A class method")

class B(object):
    def __init__(self):
        super().__init__()
        print("inside super class B")

    def showB(self):
        print("inside B class method")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("inside super class C")

    def showC(self):
        print("inside C class method")


obj = C()

# In Python, MRO stands for Method Resolution Order. It is the order in which Python looks 
# for a method in a hierarchy of classes, especially when dealing with multiple inheritance, where a method might be found in several superclasses.
b = C.mro() 
print(b)
# obj.showA()
# obj.showB()
# obj.showC()
# obj = A()
# obj = B()