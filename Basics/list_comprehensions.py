metrix = [[j for j in range(5)] for i in range(5)]
print(metrix)

matrix = []
for i in range(5):
    # Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        matrix[i].append(j)
print(matrix)

list1 = [2,5,7,3,8,4]
new_list = [item for item in list1 if item%2 == 0]
print(new_list)

def is_consonent(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


def replace(letter):
    vowels = "aeiou"
    return "*" if letter in vowels else letter


myString = "shraddha"
myName = [letter for letter in myString if is_consonent(letter=letter)]
print(myName)

myName = [replace(letter) for letter in myString]
print(myName)
