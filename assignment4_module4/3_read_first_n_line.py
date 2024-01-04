# Write a Python program to read first n lines of a file. 
inputFile = "n_lline_file.txt"

N = int(input("Enter N value: "))

with open(inputFile, 'r') as filedata:
    linesList = filedata.readlines()
    print(f"first,{N} lines of the text file:")
    for textline in linesList[:N]:
        print(textline) 
