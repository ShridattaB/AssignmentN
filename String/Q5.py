# Assignment 5: Check for Palindrome

# Instructions: Write a Python function that takes a 
# string as input and returns True if the string is a palindrome 
# (reads the same forwards and backwards), or False otherwise.

# Sample Input:
# input_string = "racecar"


# Sample Output:
# is_palindrome = True

input_string = "racecaw"
empty=""
for i in input_string:
    empty=i+empty
if empty==input_string:
    print("this is palindrone")
else:
    print("this is not palindrone")