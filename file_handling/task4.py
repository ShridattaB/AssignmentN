# Write a function count_words(file_name) that takes a file name as an argument and counts the number of words in the file.
# Use this function to count and print the number of words in the "sample.txt" file.
# Example Input:

# sample.txt (file content - same as Task 1)
# Hello, this is a sample text file.
# It contains some text for reading.

# Example Output:
# Word count in sample.txt: 11

# Explanation: In this task, the count_words function is implemented to count the words in a file.
#  In this example, there are 11 words in "sample.txt."

file= open("sample.txt","r")
data =file.read()
print("Word count in sample.txt:",file.tell())