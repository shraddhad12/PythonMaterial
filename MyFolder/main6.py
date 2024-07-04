# A =  ['a', 'b', 'c', 'd', 'e']
# B =  ['e', 'b', 'c', 'd', 'a']

# top_pages = 2
# output = []
# for i in range(len(A)-1):
#     for j in range(len(B)-top_pages):
#         if  A[i:i+top_pages] ==  B[j:j+top_pages]:
#             output.append(A[i:i+top_pages])
#         else:
#             continue
# print("Common Sequences are", output)


str1 = "1,234,567,890"
str2 = "1,234,567,890"

def adding_coma(sum):
    output = ""
    for i, c in enumerate(sum[::-1]):
        output += c
        if (i+1)%3 == 0 and i != 0:
            output += ","
    return output[::-1]

sum = str(int(str1.replace(",", "")) + int(str2.replace(",", "")))
print(sum)
output = adding_coma(sum)

print("Sum of two string is ", output)


