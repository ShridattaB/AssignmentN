# 4.1 :  Write a function that can take any number of
# arguments and returns their sum. Use *args to handle variable arguments.
# Input: sum_numbers(1, 2, 3)
# Expected Output: 6

def sum_number(*arg,name):
    sum=0
    for i in arg:
        sum=sum+i
    print(sum)
    print(name)

sum_number(1,2,3,name="hello")


