# Write a Python function that takes a list and returns a new list with unique elements of the first list.
list1=[1,2,3,4,3,2,6,7,6,8,9,10]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)