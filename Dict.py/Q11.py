# Question11: Create a program to find the keys with the top N (e.g., 3) maximum values in a dictionary.

# Sample Input: 
# Dictionary: {'a': 50, 'b': 70, 'c': 60, 'd': 70}
# N: 3

# Expected Output: 
# Keys with top 3 maximum values: ['b', 'd', 'c']

# Explanation: Find the keys associated with the top N maximum values in the dictionary

from operator import itemgetter
 
Dictionary = {'a': 50, 'b': 70, 'c': 60, 'd': 70}

N = 3

print("The original dictionary is : " + str(Dictionary))
 

res = dict(sorted(Dictionary.items(), key=itemgetter(1), reverse=True)[:N])

print("The top N value pairs are " + str(res))