
# Sample Input: 
# Dictionary 1: {'a': 1, 'b': 2}
# Dictionary 2: {'c': 3, 'd': 4}

# Expected Output: 
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

Dictionary_1= {'a': 1, 'b': 2}
Dictionary_2={'c': 3, 'd': 4}
Dictionary_1.update(Dictionary_2)
print(Dictionary_1)
print({**Dictionary_1,**Dictionary_2})