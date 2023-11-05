# Question2: Write a program to access and print the value associated with a specific key in a dictionary.
# Sample Input:
# Dictionary: {'name': 'John', 'age': 25, 'city': 'New York'}
# Key: 'age'
# Expected Output:
# The age is 25
# Explanation: The program should access the value associated with the key 'age' and print it

dict1={'name': 'John', 'age': 25, 'city': 'New York'}
# age=dict1['age']
# print("the age is ", age)
for i in dict1.items():
    print(i)


