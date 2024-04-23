class Circle:
    def __init__(self):
        self.radius = 5

    #instance method
    def area(self):
        return 3.14
circle1 = Circle()
print(circle1.area()) #instance method call using object and takes self as argument



class Circle:
    def __init__(self):
        self.radius = 5

    @classmethod
    def area(self):
        return 3.14
circle1 = Circle()
print(circle1.area()) #class method call using object and class name also takes self as argument
print(Circle.area())

class Circle:
    def __init__(self):
        self.radius = 5
    @staticmethod
    def area():
        return 3.14
circle1 = Circle()
print(circle1.area()) #static method call using object and class name and does not take self as argument
print(Circle.area())