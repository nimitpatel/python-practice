'''
Read a text file in Python and print no. of lines and no. of unique words.
                                &
Write a Python program to read a text file and do following:
1. Print no. of words
2. Print no. statements
                                &
Write a Python program to count words, characters and spaces from text file
'''

fname = "w175b.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len(words)
        num_chars += len(line)

print("No. of Lines", num_lines)
print("No. of Words", num_words)
print("No. of Characters", num_chars)
