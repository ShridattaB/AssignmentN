# Question11: Write a program to find the greatest common divisor (GCD) of two numbers using Euclidean algorithm.
# Sample Input: (Number1, Number2) = (48, 18)
# Expected Output: GCD of 48 and 18 is 6

import math
(Number1, Number2) = (48, 18) 
ans=math.gcd(Number1, Number2)
print(f"GCD of {Number1} and {Number2} is {ans}")