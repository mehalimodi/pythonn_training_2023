# Write a Python program to check whether an element exists within a tuple.
tuple=(2,42,44,21,65,54,33)
input=int(input("enter number: "))
if input in tuple:
    print("exist")
else:
    print("not exist")