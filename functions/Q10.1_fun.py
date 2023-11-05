# 10.1 write a recursion function to print 1,2,3,4,5

#       Input: printNum(5)
#      Expected Output: 1,2,3,4,5 




def numbers(n):
    if n==0:
        return
    numbers(n-1)
    print(n, end=" ")
numbers(5)

    








