# Modify the program from Task 2 to append the user
# 's input to an existing file named "user_data.txt" instead of creating a new file each time.
# Example Input:

# User Input:
# This is another user-entered sentence.

# Example Output:

# user_data.txt (file content):
# This is a user-entered sentence.
# This is another user-entered sentence.


# Explanation: In this task, the program appends the 
# user's input to the existing "user_data.txt" file instead of overwriting it
# rename name
# import os
# os.rename("user_input.txt", "user_data.txt")

# file= open("user_data.txt","a+")
# file.write("\nThis is another user-entered sentence.")
# file.seek(0)
# data=file.read()
# print("user_data.txt (file content):\n" + data)

file=open("user_data.txt","r")
print(file.read())

