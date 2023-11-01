#  Write a Python program to check whether a list contains a sub list.
list=[21,54,58,24,25,53,44]
sub_list=[54,1,2,3,44]
for i in sub_list:
    if i in list:        
        print(f"Yes it contains{i}")