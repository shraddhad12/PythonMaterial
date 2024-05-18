'''
Abstraction is one of the core principles of object-oriented programming (OOP). It involves hiding the complex 
implementation details of a system and exposing only the essential features to the users. Abstraction helps to reduce 
complexity and allows the programmer to focus on interactions at a higher level.


Key Concepts of Abstraction
Abstract Classes: An abstract class cannot be instantiated and is designed to be subclassed. It often contains one or more abstract methods.
Abstract Methods: An abstract method is a method that is declared but contains no implementation. Subclasses must override and implement these methods.
'''

'''
Encapsulation is about bundling the data and methods and controlling access to them, 
while abstraction is about hiding complex details and exposing only the necessary parts of an object. 
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("The animal is sleeping")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows")

# Usage
dog = Dog()
dog.make_sound()  # Output: The dog barks
dog.sleep()       # Output: The animal is sleeping

cat = Cat()
cat.make_sound()  # Output: The cat meows
cat.sleep()       # Output: The animal is sleeping

# The following line would raise an error because Animal is abstract and cannot be instantiated
# animal = Animal()

