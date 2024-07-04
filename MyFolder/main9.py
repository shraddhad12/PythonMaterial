matrix = [ [1,2,3,4]
          ,[4,3,2,1]
          ,[7,8,9,6]
          ,[6,5,4,3]]

principle_diag_sum = 0
secondory_diag_sum = 0

x = len(matrix[0])-1
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i == j:
            principle_diag_sum += matrix[i][j]
        if j == x :
            secondory_diag_sum += matrix[i][j]
            x -= 1
        else:
            continue
print(principle_diag_sum)
print(secondory_diag_sum)

 