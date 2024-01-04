# Write a Python program to write a list to a file.
f=open("file1.txt", "a")
list1=['hello','list to file','python']
for i in list1:
    f.write(f"{i}\n")
f.close()

f = open("file1.txt", "r")
print(f.read())