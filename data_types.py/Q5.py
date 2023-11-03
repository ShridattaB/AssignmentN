# Sample Input: Numbers = 10, 5, 8
# Expected Output: The largest number is 10

numbers=10,5,8
max_num=0
for i in numbers:
    if i > max_num:
        max_num=i
print(max_num)