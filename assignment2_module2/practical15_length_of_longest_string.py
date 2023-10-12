# Write a Python function that takes a list of words and returns the length of the longest one.
list=['fan','bike','cardboard','door','pen']
longest=0
for i in list:
    if len(i) > longest:
        longest=len(i)
        longest_word=i
print(longest_word)