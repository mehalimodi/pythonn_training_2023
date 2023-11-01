# Write a Python function that takes two lists and returns true if they have at least one common member.
list1=[1,3,4,2,5,7]
list2=[9,8,6,43,7]
for a in list1:
    for b in list2:
        if a==b:
            print("true")
        