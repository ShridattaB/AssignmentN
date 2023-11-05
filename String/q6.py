
# Instructions: Write a Python function that takes a string 
# as input and returns the longest word in the string.

# Sample Input:
# input_string = "The quick brown fox"


# Sample Output:
# longest_word = "quick"

input_string = ("The quick brown fox").split()
longest_word=""
for word in input_string:
    if len(word) > len(longest_word):
        longest_word=word
print(longest_word)

