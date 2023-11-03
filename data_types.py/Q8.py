# Sample Input: Limit = 20
# Expected Output: Fibonacci sequence up to 20: [0, 1, 1, 2, 3, 5, 8, 13]

#fibonacci series= 0,1,1,2,3,5

def fibonacci(num):
    n1,n2=0,1
    if num==1:
        print(0)
    else:
        print(n1,n2,end=" ")

        for i in range(2,num):
            n3=n1+n2
            n1=n2
            n2=n3
            print(n3,end=" ")

fibonacci(5)

