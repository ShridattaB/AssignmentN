# Question8: Implement a program to find common key-value pairs between two dictionaries.

# Sample Input: 
# Dictionary_1= {'a': 1, 'b': 2, 'c': 3}
# Dictionary_2= {'b': 2, 'c': 3, 'd': 4}

# Expected Output: 
# Common key-value pairs: {'b': 2, 'c': 3}

# Explanation: The program should identify key-value pairs that exist in both dictionaries.
Dictionary_1= {'a': 1, 'b': 2, 'c': 3}
Dictionary_2= {'b': 2, 'c': 3, 'd': 4}
for i in Dictionary_1:
    for i in Dictionary_2:
        print(i,end=" ")
