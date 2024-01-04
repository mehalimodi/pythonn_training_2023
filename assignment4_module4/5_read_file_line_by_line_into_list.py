# Write a Python program to read a file line by line and store it into a list
def read_file_into_list(file_path):
    lines_list = []
    with open(file_path, 'r') as file:
        for line in file:
            lines_list.append(line.strip())  
    return lines_list

file_path = 'read.txt'  
result = read_file_into_list(file_path)

if result is not None:
    print("File contents stored in a list:")
    for line in result:
        print(line)
