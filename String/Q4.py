# Assignment 4: Remove Duplicates

# Instructions: Write a Python function that takes a string as input and returns the string with duplicate characters removed.

# Sample Input:
# input_string = "banana"


# Sample Output:
# output_string = "ban"

input_string = "banana" 
string=""
for i in input_string:
    if i not in  string:
        string=string+i
print(string)