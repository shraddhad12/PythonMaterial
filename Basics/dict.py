d = {2: 2, 3: 5, 5: 2, 6: 4}
    
max_element = max(d, key=d.get)
max_count = d[max_element]

a=max(d, key=d.get)
print(a)

b=sum(d.values())
print(b)
print(f"The element with the maximum count is {max_element}, which appears {max_count} times.")

print("Iterating through keys:")
for key in d:
    print(f"Key: {key}")

print("Iterating through values:")
for value in d.values():
    print(f"Value: {value}")

print("Iterating through key-value pairs:")
for key, value in d.items():
    print(f"Key: {key}, Value: {value}")

sorted_by_keys = dict(sorted(d.items()))
print("Sorted by keys:", sorted_by_keys)

# Sorting by values
sorted_by_values = dict(sorted(d.items(), key=lambda item: item[1]))
print("Sorted by values:", sorted_by_values)

for i in d.items():
    print(i[0] ,i[1])

# Sorting by values in descending order
sorted_by_values_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print("Sorted by values (descending):", sorted_by_values_desc)

# Sorting a Dictionary by Keys and Values Together
unsorted_dict = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2, 'berry': 2}

# Sorted dictionary by values, then by keys
sorted_dict_by_values_keys = {key: value for key, value in sorted(unsorted_dict.items(), key=lambda item: (item[1], item[0]))}

print(sorted_dict_by_values_keys)