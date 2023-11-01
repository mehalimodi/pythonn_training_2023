# Write a Python program to remove duplicates from a list. 
l1=[32,74,83,70,32]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)