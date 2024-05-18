'''
Hybrid inheritance is a combination of two or more types of inheritance. 
It aims to leverage the benefits of different inheritance types while maintaining the structure and organization of the classes.
'''

class Base:
    def base_method(self):
        print("This is the base method")

class Derived1(Base):
    def derived1_method(self):
        print("This is the derived1 method")

class Derived2(Base):
    def derived2_method(self):
        print("This is the derived2 method")

class MultiDerived(Derived1, Derived2):
    def multi_derived_method(self):
        print("This is the multi-derived method")

# Usage
m = MultiDerived()
m.base_method()         # Inherited from Base
m.derived1_method()     # Inherited from Derived1
m.derived2_method()     # Inherited from Derived2
m.multi_derived_method()  # Defined in MultiDerived
