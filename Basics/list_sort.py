mylist = [1, 5, 6, 8, 3, 5, 9, 0]
print(mylist.sort())   #print None ----This returns nothing , will only update original list

print(mylist) # print sorted array


mylist = mylist + [10, 5]
print(mylist)

#But here I can't add elements of list using append
mylist.append([10,11]) #This function returns None
print(mylist)  # output [0, 1, 3, 5, 5, 6, 8, 9, 10, 5, [10, 11]]
 


