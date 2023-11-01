# Write a Python program to check multiple keys exists in a dictionary.
a={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}
count=0
for k in a:
    count+=1
if count>1:    
    print("Multiple Keys are present")    
else:
    print("Multiple Keys are not present")    