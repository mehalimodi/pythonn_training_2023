# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
n=int(input("enter number:"))
a=str(n)
b=a+a
c=a+a+a
x=int(a)
y=int(b)
z=int(c)

total=x+y+z
print(f"total: {x} + {y} + {z} = {total}")
