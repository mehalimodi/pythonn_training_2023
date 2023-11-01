#  Write a Python program to find the highest 3 values in a dictionary.
a={'A':55,'B':56,'C':96,'D':91,'E':84}
values = list(a.values())

#sort the values in descending order
values.sort(reverse=True)

#print the first three values from dictionary
highest_3_values = values[:3]

print("The highest 3 values in the dictionary are:")
for value in highest_3_values:
    print(value)