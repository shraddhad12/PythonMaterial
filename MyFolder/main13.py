

# # list1 = [1,2,3,4,5,6,7,8,9]
# # result = list(filter(lambda x: x%3==0, list1))
# # print(result)


# l1=[1,2,3]
 
# l2=[3,4,5]
 
# l3=l1
  
# l4=l2[:] #[3,4,5]
 
# l3[0]=3 # [3, 2, 3]
 
# l4[0]=1 #[1,4,5]


# l1 = l3 = [3, 2, 3]
# l2 =[3,4,5]
# l4= [1,4,5]

number = "15"
string = list(number)
print(string)
if "-" in string or "+" in string:
    sign =string[0]
    string.pop(0)
    reverse = string[::-1]
    reverse = sign + "".join(reverse)

else :
    reverse  =number[::-1]
print(reverse)

db.customer.find(user_id=123).count()

