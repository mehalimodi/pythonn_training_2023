# Write a Python script to check if a given key already exists in a dictionary. 
a={'python':60,'java':56,'.net':79}
input=input("enter a key: ")
if input in a.keys():
    print("exist")
else:
    print("not exist")