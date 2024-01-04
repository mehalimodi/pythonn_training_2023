# Write a Python program to count the frequency of words in a file. 
def countword(filename):
    word_counts = {}

    with open(filename, 'r') as f:
        for line in f:
            for word in line:
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
        return word_counts

filename = "frequency_of_words.txt"
word_counts = countword(filename)
# total_words = sum(word_counts.values())

print(f"The file {filename} has {word_counts} words.")
