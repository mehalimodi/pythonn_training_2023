#  Write a Python program to print all unique values in a dictionary. 
a={1:'a',2:'b',3:'c',4:'d',5:'a',6:'f',7:'b'}
print("Original Dictionary : ",a)
#dictionary to set to find unique values
uniq_values = set(a.values())

print("Unique Values : ",uniq_values)