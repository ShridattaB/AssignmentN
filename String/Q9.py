# nstructions: Write a Python function that takes a string as input 
# and returns the count of words in the string.

# Sample Input:
# input_string = "This is a sample sentence."


# Sample Output:
# word_count = 5
def word_count(str):
    return len(str.split())
print(word_count("This is a sample sentence."))


# input_string = "This is a sample sentence."
# words=input_string.split()
# print(len(words))


