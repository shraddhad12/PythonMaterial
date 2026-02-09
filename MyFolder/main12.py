
##insife
def dec_func(func):
    def wrapper(x,y):
        print(f"Addition of {x}, {y}")
        result = func(x,y)
        print(result)
    return wrapper

@dec_func
def sum(a, b):
    return a+b

sum(4,5)

# try:

# finally:
# else

import abc
class Abstract(abc):

    @abstractmethod
    def method1(self):
        pass

    def method2(self):
        print("abstract method2")

class Class2(Abstract)
    
use python3.10
RUN as img1
mkdir /app
COPY . /app
pip install -r requirement.txt
CMD ["python", "main12.py", host = 0.0.0.0, port= 8080]