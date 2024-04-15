list = [10, 20, 396, 445, 56, 78]

list.sort()
print(f"Max number is {list[-1]} in list {list}")

## OR

temp = list[0]
max = 0
for i in list:
    if i > temp:
        max = temp
    else:
        continue
print(f"Max number is {list[-1]} in list {list}")