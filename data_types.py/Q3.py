# Sample Input: Number = 5
# Expected Output: Factorial of 5 is 120.
number=5
fact=1
for i in range(1,number+1):
    fact=fact*i
print(f"factorial of {number} is {fact}")
