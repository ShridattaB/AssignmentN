# Task 5: File Copy

# Write a function copy_file(source, destination) that takes the names of two files as arguments and copies the content of the source file to the destination file.
# Use this function to copy the contents of "sample.txt" to a new file named "sample_copy.txt."

# Example Input:

# sample.txt (source file, content same as Task 1)

# Example Output:

# sample_copy.txt (destination file, content same as Task 1)

# Hello, this is a sample text file.
# It contains some text for reading.


# Explanation: In this task, the copy_file function is implemented to copy the content of one file to another. In this example, the content of "sample.txt" is copied to "sample_copy.txt."

file1=open("sample.txt","r")
file2=open("sample_copy.txt","w")
for i in file1:
    file2.write(i)

