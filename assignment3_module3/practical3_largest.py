list=[]
sum=0
for i in range(1,6):
    num=int(input("enter number:"))
    sum+=num
    list.append(num)
print("maximum number:",max(list))
print("minimum number:",min(list))
print("the of numbers is:",sum)
    