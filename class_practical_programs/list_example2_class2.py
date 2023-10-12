'''shopping_list=["tv","radio"]
status=True
while status:
    product_name=input("enter the product name: ")
    shopping_list.append(product_name)
    choice=input("do you want to add more product : press y for yes or n for no: ")
    if choice=='n':
        status=False
# print(shopping_list)
for item in shopping_list:
    print(item,end=",")'''



# extend example
'''l1=[1,2,3,4]
l1.extend([22,33,44])
print(l1)'''


# insert example
'''l1=[1,2,3,4]
l1.insert(2,333)
print(l1)'''

# task
name=[]
status=True

while status:
    for i in range(1,6):
        list_name=input("enter your name: ")
        name.append(list_name)
    status=False
    '''choice=input("do you want to add more product : press y for yes or n for no: ")
    if choice=='n':
        status=False'''
for list_name in name:
    print(list_name)


