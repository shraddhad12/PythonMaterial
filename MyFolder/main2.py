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