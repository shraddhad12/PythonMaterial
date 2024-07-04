def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class SingletonClass:
    def __init__(self, value):
        self.value = value

# Usage
singleton1 = SingletonClass(1)
singleton2 = SingletonClass(2)

print(singleton1.value)  # Output: 1
print(singleton2.value)  # Output: 1
print(singleton1 is singleton2)  # Output: True