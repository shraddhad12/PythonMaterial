def armstrong(num):
    n = num
    l = len(str(num))
    sum = 0
    while num != 0:
        a = num % 10
        sum = sum + a**l
        num = num //10
    if n == sum:
        return "armstrong"
    else:
        return "not armstrong"

num = 153
am = armstrong(num)
print(f"Given number {num} is", am)