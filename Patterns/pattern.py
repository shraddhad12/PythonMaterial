for i in range(10):
    for j in range(10):
        print(end=" * ")
    print()

print()
print()
print()

for i in range(10):
    for j in range(10):
        if i>j:
            print(end=" * ")
    print()

print()
print()
print()

for i in range(10):
    for j in range(1, 10):
        if i>j:
            print(end=str(j))
    print()

print()
print()
print()

for i in range(10):
    for j in range(10):
        if i<j:
            print(end=" * ")
    print()

print()
print()
print()

for i in range(10):
    for j in range(i+1):
        print(end=str(j+1))
    print()

print()
print()
print()

for i in range(10):
    for j in range(1, 10 - i):
        print(" ", end="")
    for j in range(i + 1):
        print(j + 1, end="")
    print()


n=10
for i in range( n):
    for j in range(n - i - 1):
        print('  ', end='')
    for j in range(2 * i + 1):
        print('* ', end='')
    print()