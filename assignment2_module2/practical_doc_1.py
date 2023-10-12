# Write a Python program to sort three integers without using conditional statements and loops
a=int(input("enter first input:"))
b=int(input("enter second input:"))
c=int(input("enter third input:"))

a1=min(a,b,c)
b1=max(a,b,c)
c2=(a+b+c)-a1-b1
print("sorted int:",a1,b1,c2)