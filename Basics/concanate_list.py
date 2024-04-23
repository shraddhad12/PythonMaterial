lst1 = ['W', 'a', 'w', 'b']
lst2 = ['e', ' ', 'riting', 'log']

# for i in zip(lst1, lst2):
#     print(i)
lst3 = [x + y for x, y in zip(lst1, lst2)]
print(lst3)