'''
In hierarchical inheritance, multiple classes inherit from a single superclass. This allows the same base class to be used by multiple derived classes.
'''

class Parent:
    def parent_method(self):
        print("This is the parent method")

class Child1(Parent):
    def child1_method(self):
        print("This is the child1 method")

class Child2(Parent):
    def child2_method(self):
        print("This is the child2 method")

# Usage
c1 = Child1()
c1.parent_method()  # Inherited from Parent
c1.child1_method()  # Defined in Child1

c2 = Child2()
c2.parent_method()  # Inherited from Parent
c2.child2_method()  # Defined in Child2