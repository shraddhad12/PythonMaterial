import pandas as pd

df = pd.read_csv("test.csv")


max_weight = df.agg({'weight': 'max'})
max_weight = df['weight'].max()
# print(max_weight)
print(df[df['weight']==max_weight])


r = df.groupby('sector').agg({'weight': [sum, max]})
# print(r)

s="fed#dsws#dwd"
x=s.count("#")
s=s.replace("#","")
print("#"*x+s)


n=10
arr=list(map(int,input().split()))
dup=[]
print(arr)
for i in arr:
    if(i not in dup):
        dup.append(i)
        print(arr.count(i))
        print("{} occurs {} times".format(i,arr.count(i)))


def sum_dec(fun):
    def wrapper(a, b):
        return fun(a, b, a+b)
    return wrapper

@sum_dec
def sum(a, b, result):
    return result

print(sum(2, 4))


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in range(len(list(s))-1):
            for j in range(1, len(list(s))-i):
                if s[i:j] == s[j:i+1:-1]:
                    return s[i:j]
                else:
                    continue
        return s
        

s = "babad"
# s = "abcdef"
print(Solution().longestPalindrome(s))

import pandas as pd

dic = {"name": ["vishal", "shraddha", "sonu"], "age": [21, 23], "department": ["cse", "it", "finance"], "company": ["HelloVerify"]}

df = pd.DataFrame.from_dict(dic, orient='index').transpose()
print(df)

import numpy as np

# Define lists of different lengths
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston']

# Create a dictionary
data = {
    'Name': names,
    'Age': ages,
    'City': cities
}

# Create a DataFrame
max_length = max(len(data[key]) for key in data)

for key in data:
    data[key] += [np.nan] * (max_length - len(data[key]))

df = pd.DataFrame(data)
print(df)
