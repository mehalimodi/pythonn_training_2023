'''number=int(input("Enter the range: "))'''
number1=0
number2=1
count=0
n=10
temp=number2
while count<=n:
    print(temp,end=" ")
    count+=1
    number1,number2=number2,temp
    temp=number1+number2
print()