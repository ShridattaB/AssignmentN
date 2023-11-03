
# Question7: Write a program to find the common elements between two lists.

# Sample Input: List1 = [1, 2, 3, 4], List2 = [3, 4, 5, 6]
# Expected Output: Common elements: [3, 4]

List1 = [1, 2, 3, 4]
List2 = [3, 4, 5, 6]
common= list(set(List1).intersection(List2))
print(common)