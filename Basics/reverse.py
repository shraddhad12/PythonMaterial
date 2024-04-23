# Reverse list using slicing method
def reverse_list(lst):
    r = lst[::-1]
    return r

# Reverse list using reverse method
def reverse_list2(lst):
    lst.reverse()
    return lst

# Reverse string using slicing method
def reverse_string(str):
    r = str[::-1]
    return r


lst = [10, 11, 12, 13, 14, 15]
print("List before reversing", lst)
print("List after reversing", reverse_list(lst))
print("List after reversing 2", reverse_list2(lst))

str = "Hello World"
print("String before reversing", str)
print("String after reversing", reverse_string(str))


s="I.like.this.program.very.much"
s = s.split('.')
s = s[::-1]
s = '.'.join(s)
print(s)