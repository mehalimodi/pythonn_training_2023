# Write a Python program to count the number of lines in a text file. 
def count_lines(filename):
  
  with open(filename, 'r') as f:
    lines = 0
    for line in f:
      lines += 1
  return lines

filename = "count_lines.txt"
number_of_lines = count_lines(filename)
print(f"The file {filename} has {number_of_lines} lines.")
