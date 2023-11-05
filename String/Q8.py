
# Assignment 8: Title Case

# Instructions: Write a Python function that takes a string as input and returns the string in title case (capitalize the first letter of each word).

# Sample Input:
# input_string = "the quick brown fox"


# Sample Output:
# output_string = "The Quick Brown Fox"

input_string = "the quick brown fox".split()
for i in input_string:
    new_varible=i.title()
    new_varible="".join(new_varible)
    print(new_varible,end=" ")



