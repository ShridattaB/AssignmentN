# Assignment 3: Count the Number of Vowels

# Instructions: Write a Python function that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.

# Sample Input:
# input_string = "hello, world!"


# Sample Output:
# vowel_count = 3

input_string = "hello, world!"
count=0
for i in input_string:
    if i in "aeiou":
        count=count+1
print(count)
