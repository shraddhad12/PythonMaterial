class Destructor:
    def __init__(self):
        self.a=10

obj = Destructor()
print(obj.a)
del(obj)
print(obj.a) ## Throw - NameError: name 'obj' is not defined
