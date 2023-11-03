# Question10: Write a program to sort a dictionary by its values in descending order.

# Sample Input: 
# Dictionary: {'a': 10, 'b': 30, 'c': 20, 'd': 5}

# Expected Output: 
# Sorted dictionary by values: {'b': 30, 'c': 20, 'a': 10, 'd': 5}

Dictionary={'a': 10, 'b': 30, 'c': 20, 'd': 5}
new= list(Dictionary.values())
print(new)