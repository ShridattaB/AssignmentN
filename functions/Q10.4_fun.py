# 10.4: Implement a recursive function to 
# find the nth Fibonacci number. Optimize it 
# using memoization to improve performance.

#      Input: fibonacci(5)
#      Expected Output: 5

def fibonacci(n):
    if n<=1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n=10 
for i in range(n):
    print(fibonacci(i) ,end=" ")





