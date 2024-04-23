import random
from itertools import permutations
def perm(str):
    if len(str) == 0:
        return ['']
    if len(str) == 1:
        return [str]
    l = len(str)
    list = []
    p = []
    while len(p) != factorial(l):
        str = shuffle(str)
        if str not in list:
            p.append(str)
            list.append(str)
        continue
    return p
        

def shuffle(str):
    str_list = list(str)
    random.shuffle(str_list)
    return ''.join(str_list)
        
        
def factorial(l):
    if l == 0:
        return 1
    return l * factorial(l-1)

for i in perm('abb'):
    print(i)

def find_permutation(s):
    perm = permutations(str)
    l=[]
    for i in perm:
        i = ''.join(i)
        if i not in l:
            l.append(i)
    return l

for i in find_permutation('abb'):
    print(i)

    