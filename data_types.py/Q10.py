# Question10: **Implement a program to find and display prime numbers up to a given limit.

# Sample Input: Limit = 30
# Expected Output: Prime numbers up to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

for num in range(30):
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num, end=" ")

