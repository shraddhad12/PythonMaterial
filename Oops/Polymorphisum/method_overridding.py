'''
Method overriding is a concept in object-oriented programming where a subclass provides a specific implementation of a method that is already defined in its superclass. 
The overridden method in the subclass should have the same name, return type, and parameters as the method in the superclass. 
This allows the subclass to provide its own behavior while retaining the same method signature.

Key points
1. Same Method Signature
2. Inheritance
3. can use super keyword to call the overridden method in the superclass from the subclass.

Why Use Method Overriding?
Polymorphism:allowing you to use a single interface while having multiple implementations.
Code Reusability: You can extend the functionality of a superclass without modifying its code, promoting code reuse and reducing redundancy.
Custom Behavior: Subclasses can provide specific behavior that is different from the superclass, making the subclass more specialized.
'''


class Bird:
  
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
  
    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):

    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Initialize the superclass
        self.breed = breed

    def speak(self):
        super().speak()  # Call the superclass method
        print(f"{self.name} barks. Breed: {self.breed}")

# Usage
dog = Dog("Rex", "Labrador")
dog.speak()  # Output:
             # Rex makes a sound
             # Rex barks. Breed: Labrador

