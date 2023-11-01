# Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} 
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 

dict1 = {'maths': 90, 'science': 204, 'b': 350}
dict2 = {'maths': 100, 'science': 200, 'english': 300}
 
 
# adding the values with common key
for a in dict2:
    if a in dict1:
        dict2[a] = dict2[a] + dict1[a]
    
print(dict2)