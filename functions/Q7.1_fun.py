# 7.1: Define a higher-order
# function that takes a list of
# integers and a function (e.g., sum, product) 
# as arguments and applies
# the function to the list.

# Input: apply_function([1, 2, 3, 4], sum)
# Expected Output: 10
 
# def sum_of_num(*a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     return(sum)


# list=[1,2,3,4,5]
# apply_function=list
# print(apply_function,sum_of_num(list))


# def is_even(n):
#     ans= n%2==0
#     return ans
# numbers=[1,2,3,4,5,6,7,8]
# events=list(filter(is_even,numbers))
# print(events)

# def is_even(args):
#     if args%2==0:
#         return args
# list1=[1,2,3,4,5,67,8]

# even=list(filter(is_even,list1))
# print(even)


    # Input: apply_function([1, 2, 3, 4], sum)
    #    Expected Output: 10

# def sum_and_multiply(num):
#     add=0
#     for i in num:
#         add=i+add
#     multi=1
#     for i in num:
#         multi=i*multi
#     return add
# def operation(num,fun):
#     return fun(num)
# print(operation([2,3,4],sum_and_multiply))







# def multiply(num):
#     multi=1
#     for i in num:
#         multi=i*multi
#     return multi
# def operation(num,fun):
#     return fun(num)
# print(operation([2,3,4],multiply))



def sum(num):
    add=0
    for i in num:
        add=add+i
    return add
def multiply(num):
    multi=1
    for i in num:
        multi=multi*i
    return multi
def operation (num,fun):
    if len(num)==0:
        return("list is empty")
    return fun(num)
print(operation([],sum))
print(operation([2,3,4],multiply))