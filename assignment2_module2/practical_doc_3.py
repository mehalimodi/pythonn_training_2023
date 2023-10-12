# Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.
a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))

if a==b or b==c or c==a:
    print("equal")
    sum=0
else:
    sum=a+b+c
print(f"sum: {a} + {b} + {c} = {sum}")