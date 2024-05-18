'''
In multilevel inheritance, a class is derived from another class, which is also derived from another class. This forms a chain of inheritance.
'''

class Grandparent:
    def grandparent_method(self):
        print("This is the grandparent method")

class Parent(Grandparent):
    def parent_method(self):
        print("This is the parent method")

class Child(Parent):
    def child_method(self):
        print("This is the child method")

# Usage
c = Child()
c.grandparent_method()  # Inherited from Grandparent
c.parent_method()       # Inherited from Parent
c.child_method()        # Defined in Child