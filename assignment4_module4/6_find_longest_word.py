# Write a python program to find the longest words. 
text = input("Enter a string: ")
words = text.split()

longest_word = max(words, key=len)

print(f"The longest word(s) is/are: {longest_word}")

