
# Sample Input: 
# Dictionary: {'a': 10, 'b': 30, 'c': 20}

# Expected Output: 
# Key with the highest value: 'b'

# Dictionary={'a': 10, 'b': 30, 'c': 20}
# num=(max(Dictionary.values()))
dictt = {'a': 10, 'b': 30, 'c': 201}
Key_max = max(dictt, key = lambda x: dictt[x])  
print("The key with the maximum value is: ", Key_max)  


