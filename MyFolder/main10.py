def dec_func(func):
    print("Before")
    def wrapper(*args):
        func()
        print("Before")
    return wrapper

@dec_func
def say_hello():
    print("Hello")

say_hello()

l = [1,2,3,4]
even = list(map(filter(lambda x: x*x , l)))
print(even)


Orders 
id prod_id quantity
1  x        2
1  y        5

Products
prod_id price
x       30
y       10

SELECT ID, SUM(PRICE * QUANTITY)
FROM ORDERS AS O
JOIN PRODUCTS AS P O.PROD_ID = P.PROD_ID
GROUP_BY O.ID

OUTPUT

id  PRICE
1   