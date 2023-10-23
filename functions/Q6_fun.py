# 6: Create a function that takes a list 
# of numbers as an argument and returns the sum and average of the numbers.

#     nput: sum_and_avg([1, 2, 3, 4, 5])
#      Expected Output: (15, 3.0)

def sum_avg(*args):
    sum=0
    avg=0
    length=len(args)
    for i in args:
        sum=sum+i
    avg=sum/length

    print(sum,avg)

sum_avg(1,2,3,4,5)