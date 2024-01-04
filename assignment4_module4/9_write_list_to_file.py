# Write a Python program to write a list to a file. 
list=["name","subject","marks","city"]

with open('abc.txt', "w") as myfile:
    for c in list:
        myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())