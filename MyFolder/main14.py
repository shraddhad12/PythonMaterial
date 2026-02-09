
string = "AABBBCCCTA"
list1 = list(string)
output = ""
count = 1
for i in range(len(list1)-1):
    letter = list1[i]
    if list1[i] == list1[i+1]:
        count += 1
    else:
        output += letter + str(count)
        count = 1
    if :
        print("last element")
        print(output)
        output += letter + str(count)
print(output)
