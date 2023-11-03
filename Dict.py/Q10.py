# Question10: Write a program to sort a dictionary by its values in descending order.

# Sample Input: 
# Dictionary: {'a': 10, 'b': 30, 'c': 20, 'd': 5}

# Expected Output: 
# Sorted dictionary by values: {'b': 30, 'c': 20, 'a': 10, 'd': 5}

Dictionary={'a': 10, 'b': 30, 'c': 20, 'd': 5}
def sort_len(a):
    return a[1]
new_dict=sorted(Dictionary.items(),key= sort_len,reverse=True)
print(new_dict)

# import operator
# d= {1:2,3:4,4:3,2:1,0:0}
# print("origin dictonary",d)

# sorted_d= sorted(d.items(),key=operator.itemgetter(1))
# print("DIctonary in asending by value",sorted_d)

# sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
# print("dictonary in descending",sorted_d)