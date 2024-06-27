# n=10
# for i in range(n):
#     for j in range(i, n):
#         if i < j:
#             print("* ", end="")
#     print("")

# list1= [3,5,11,50]
# list2=[1,4,7,9,13,22]

# list3=list1+list2
# list3.sort()
# print(list3)

import pandas as pd
dic = [{"a": 1, "b":2}]
df = pd.DataFrame(dic)
print(df)


print(df.loc[0,"a"])

# print(df)


# try:
#     a =10/0
#     print(a)
# except Exception e:

# finally:
    

