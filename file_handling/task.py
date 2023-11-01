# Task 1: File Reading
# Create a Python program that reads a text file named "sample.txt."
# Print the contents of the file to the console.
# Example Input:
# sample.txt (file content):
# Hello, this is a sample text file.
# It contains some text for reading.

# Example Output:

# Contents of sample.txt:
# Hello, this is a sample text file.
# It contains some text for reading.

# Explanation: In this task, the program reads the content of the "sample.txt" 
# file and prints it to the console.

#-------------------------------------------------------------------------------------------
file= open("sample.txt","r")
data=file.read()
print("Contents of sample.txt:\n"+ data)
