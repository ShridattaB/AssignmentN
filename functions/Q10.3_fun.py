
# 10.3: Implement a recursive
# function to calculate the factorial of 
# a given number.

# Input: factorial(5)
# Expected Output: 120

# def fact(n):
#     if n==1:
#         return n
#     else:
#         return n * fact(n-1)
    
# print(fact(4))


def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(4))





























