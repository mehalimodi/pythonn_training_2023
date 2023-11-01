# Write a Python program to unzip a list of tuples into individual lists. 
list_of_tuples = [(1, 'a', "hello"), (2, 'b', "world"), (3, 'c', 2.0)]
first_elements = []
second_elements = []
third_elements = []
for tuple in list_of_tuples:
    first_elements.append(tuple[0])
    second_elements.append(tuple[1])
    third_elements.append(tuple[2])
    
print("List of elements:", first_elements,"," ,second_elements,",", third_elements)
