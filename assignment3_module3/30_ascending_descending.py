# Write a Python script to sort (ascending and descending) a dictionary by value.
my_dict={"A" : 1, "B" : 2,"D" : 4, "C" : 3,"F" : 6, "E" : 5}

print(my_dict)
ascending= sorted(my_dict.items())
print("Ascending : ",ascending)
descending= sorted(my_dict.items(), reverse=True)
print("Descending : ",descending)