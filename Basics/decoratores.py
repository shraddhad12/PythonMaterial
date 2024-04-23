def adv_add(fun):
    fun()

@adv_add
def add(x, y):
    return x + y

print(adv_add(add(5, 6)))

# def dec(fun):
#     print("this is addintion method")
#     fun()

# @dec
# def sum(x, y):
# 	print(x+y)

# dec(sum(5, 6))
	
	
