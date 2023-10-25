# 10.2 write a recursion function to print 10,8,6,4,2

#       Input: printResEveNum(10)
#      Expected Output: 10,8,6,4,2



def print_reverse_even_numbers(n):
    if n >= 2:
        print(n)
        print_reverse_even_numbers(n - 2)
    elif n == 1:
        print(n)

print_reverse_even_numbers(10)
