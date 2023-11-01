# How will you create a dictionary using tuples in python.
# Write a Python program to convert a list of tuples into a dictionary.
tuple=(("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30))
print(tuple)
dictionary = {}
for key, val in tuple:
    dictionary[key]=val
print(dictionary)