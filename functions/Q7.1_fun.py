# 7.1: Define a higher-order
# function that takes a list of
# integers and a function (e.g., sum, product) 
# as arguments and applies
# the function to the list.

# Input: apply_function([1, 2, 3, 4], sum)
# Expected Output: 10

def sum(num):
    sum=0 
    for i in num:
        sum=sum+i
    print(sum)

def product(num):
    multi=1
    for i in num:
        multi=multi*i
    print(multi)

def apply_function(num,fun):
    fun(num)

# def apply_function(num,fun):
#     fun(num)

apply_function([1,2,3,4],sum)
apply_function([1,2,3,4],product)