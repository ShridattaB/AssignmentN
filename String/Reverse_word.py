# Assignment 10: Reverse Words

# Instructions: Write a Python function that takes a string as input and reverses the order of words in the string.

# Sample Input:
# input_string = "Hello World"


# Sample Output:
# output_string = "Hello World"
# words= output_string.split()
# words=list(reversed(words))
# print(" ".join(words))

def reverse_word(n):
    m=n.split()
    m=list(reversed(n))
    print("".join(m))

output_string = "Hello World"
reverse_word(output_string)

output_string = "Hello World".split()
variable=output_string[::-1]
print(" ".join(variable))





