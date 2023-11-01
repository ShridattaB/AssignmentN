# Write a Python program that asks the user to enter a sentence.
# Create a new text file named "user_input.txt" and write the user's input to the file.

# Example Input:

# User Input:
# This is a user-entered sentence.

# Example Output:

# user_input.txt (file content):
# This is a user-entered sentence.

# Explanation: In this task, the program takes input from the user, 
# creates a new file "user_input.txt," and writes the user's input to the file.


file=open("user_input.txt", "w+")
file.write(input())
file.seek(0)
print("user_input.txt (file content):\n" + file.read())





