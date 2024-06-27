# class Employee:

#     def __new__(self, id):
#         return Employee()

#     def __init__(self):
#         self.id = 0
#         self.name = ""
#         self.department = ""

#     def create_employee(self, id, name, department):
#         try:
#             if id < 1:
#                 raise ValueError("id is not valid")
#             self.id = id
#             self.name = name
#             self.department = department
#             print("Employee created")
#         except ValueError as e:
#             print(e)
    
# e = Employee()
# e.create_employee(0, "shraddha", "IT")

a=10
b=5
try:
    c = a/b
    print(c)
except:
    print("Error")
else:
    print("Else")
finally:
   print("finally")

# class Dog:
    
#     def __init__(self, name, age, gender):
#         self.name = name 
#         self._age = age
#         self.__gender = gender

#     def get_gender(self):
#         return self.__gender

# class A:
#     def __new__(self):
#         return Dog()