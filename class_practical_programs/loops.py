'''for i in "python":
    print(i)'''
# range------------------------------
'''for i in range(1,11):
    print(i)'''

# jump
'''for i in range(2,21,2):
    print(i)'''

# task-------------------
'''for i in range(21,2,-2):
    print(i)'''

# task 2
'''i=int(input("enter the range:"))
for i in range(1,i+1):
    print(i)'''

# task3
'''number=int(input("Enter the value:"))
sum=0
for i in range(1,number+1):
    sum=sum+i
    print(sum)'''

# task 4
# num=int(input("enter the value:"))
# even=0
# odd=0
'''for i in range(1,num+1):
    if i%2==0:
        even=num+i
    else:
        odd=num+i
print("even sum:",even)
print("odd sum:",odd)'''


# for example
'''for i in range(1,6):
    print(i,end=" ")'''


# enter name by range
'''for i in range(1,6):
    name=input("enter you name:")'''

# rows and columns
'''for row in range(1,6):
    for col in range(1,6):
        print(" * ",end=" ")
    print()'''

# pattern star
'''for row in range(1,6):
    for col in range(1,row+1):
        print("*",end=" ")
    print()'''

# 
'''for row in range(1,6):
    for col in range(1,row+1):
        print(row,end=" ")
    print()'''

# 
'''for row in range(1,6):
    for col in range(1,row+1):
        print(col,end=" ")
    print()
'''
# 
for row in range(1,6):
    for col in range(1,row+1):
        if row%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()

for row in range(1,6):
    for col in range(1,row+1):
        if col%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
    print()













