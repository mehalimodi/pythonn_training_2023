# Write a Python program to find the repeated items of a tuple.
tuple=('apple','mango','kiwi','mango','banana','orange','apple')
print(tuple)
for i in tuple:
    if tuple.count(i) > 1:
        print(i)
