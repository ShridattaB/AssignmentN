# Question6: Implement a program to reverse a given string.

# Sample Input: String = "Python"
# Expected Output: Reversed String: nohtyP


name="Python"
str=""
for i in name:
    str=i+str
print(str)