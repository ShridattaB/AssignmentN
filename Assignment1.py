# Operator Questions

# Arithmetic Operators:
# it is uesd to perform a mathmatical expressions

# a) Write a Python program to perform addition and subtraction of two numbers entered by the user.
# a=int(input("enter The First NUmber:-"))
# b=int(input("enter The second NUmber:-"))
# c=a+b
# print("the addition of", a , b ,"is:- ",c)

# b) Calculate the area of a circle using the radius provided by the user. Use the arithmetic operators.
# r= int(input("enter the radius"))
# area= 3.14*r*r
# print("Area of trangle is:-", area)

# *Comparison Operators:*
#comparision operator is used to compare two values 

# a) Write a Python program to compare two numbers and print whether they are equal or not.
# a=3
# b=6
# if a==b:
#     print("a is equla to b")
# else:
#     print("a is not equal to b")

# b) Write a program to compare the ages of two people and print who is older.
# Age_person1= int(input("age of first Person"))
# Age_person2= int(input("age of seconf Person"))
# if Age_person1> Age_person2:
#     print("person 1 is older than person 2")
# else:
#     print("person 2 is oldaer than person 1")

# *Logical Operators:*
# logical operatores ae used to combine condition statement

# a) Write a Python program to check if a given number is in the range 10-20 (inclusive) or 30-40 (inclusive).
# num= 26
# if (num>=10 and num<=20 ) or (num>=30 and num <=40):
#     print("num is in range")
# else:
#     print("num is not in range")

# b) Write a program that checks whether a user-provided number is positive and odd.
# a=13
# if a>0 and a%2==1:
#     print("the num is positive and odd")


# *Assignment Operators:*
# this operator is used to assign the value to operator
# a) Implement a Python program that performs a compound assignment operation on a variable.
# a=4
# b=4
# a=a+b+5
# b=a+b+4
# print(a," ", b)
# b) Write a program to increment a number by 5 using the assignment operator.
# a=4
# a=a+5 
# print(a)

# *Bitwise Operators:*
# a) Perform bitwise AND operation # Display the result
# num1 = 5
# num2 = 1  
# result = num1 & num2
# print(result)

# *Bitwise Operators:*
# bitwise operator are used to compare binary number 
# b) Implement a program to toggle the nth bit of a number.

# num1 = 5
# num2 = 1  
# result = num1 ^ num2
# print(result)



# *Identity Operators:*

# a) Write a Python program to demonstrate the use of the is operator.
# Identity operators are used to compare the objects,
# not if they are equal, but if they are actually the same object, with the same memory location:


# a=12
# b=12
# print(a is  b)
# b) Write a program to compare the identities of two different lists.

# a= [1,2,3]
# b=[1,2,3]
# print(a is b)

# *Membership Operators:*
# Membership operators are used to test if a sequence is presented in an object

# a) Write a program to check if a given element exists in a list.
# a=[2,3,4,5,6]
# if 10 in a :
#     print("the value is in a ")
# else:
#     print("the value is not into a")
# b) Implement a Python program to check membership in a set.
# the_set={2,3,4,5,6,6}
# print( 6 in the_set)
# print(9 in the_set)

# *String Operators:*

# a) Write a program to concatenate two strings.
# first_name = "shridatt"
# last_name= " Bhimanavaru"
# print("Full name is ", first_name+ last_name)
# b) Implement a program to repeat a string a specified number of times.
# a= "shridatt"
# for i in range(10):
#     print(a)

# *List Operators:*
# a) Write a program to add an element at the end of a list.
# list1= [2,3,4,5]
# list1.append(3)
# print(list1)
# b) Implement a Python program to concatenate two lists.
# list1= [2,"name ",3]
# list2=[3,"sohel",43]
# list1.extend(list2)
# print(list1)

# *Ternary Operator:*
# shorter way of writing an if and if…else statement
# a) Write a Python program that uses the ternary operator to determine the maximum of two numbers.
# num1=20
# num2=30
# result= "num1 is greater" if num1> num2 else "num2 is greater"
# print(result)

# b) Write a program to determine if a given number is even or odd using the ternary operator.
# num=20
# result= "even" if num%2==0 else "odd"
# print(result)

# *Exponentiation Operator:*

# a) Write a Python program to calculate the power of a number using the exponentiation operator.
# print(10**2)
# b) Implement a program to find the square root of a number using the exponentiation operator.
# num=100

# print(num**0.5)

# Nikunj Patel — Yesterday at 4:41 PM
# Loop Questions

# For Loop:

# a) Write a Python program to print numbers from 1 to 10 using a for loop. 
# num=1
# for i in range(num,11):
#     print(i ,end=',')

# Expected Output: Here are the numbers from 1 to 10: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# b) Implement a program to calculate the factorial of a given number using a for loop.

# num= 5
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

# Test Case 1:
# Input for factorial calculation: 5
# Expected Output: A factorial of 5 is 120
# Nested For Loop:

# a) Write a program to print a multiplication table from 1 to 10 using a nested for loop.
# num=10
# for i in range (1,num+1):
#     for j in range(1,num+1):
#         print(f"{i}*{j}={i*j}")
#     print()

# Test Case 1:

# Input for multiplication table: 5
# Expected Output: Multiplication table for 5:
# num=5
# for i in range(1,num+1):
#     print(f"{num}*{i}={num*i}")

# 1 x 5 = 5
# 2 x 5 = 10
# ...
# 10 x 5 = 50

# b) Implement a Python program to print a pattern of numbers using a nested for loop.

# Input for pattern: 4
# Expected Output:
# 1
# 22
# 333
# 4444
# num=4
# for i in range(num+1):
#     for j in range(i):
#         print(i,end="")
#     print()

# a **While Loop:**

# a) Write a Python program to print numbers from 1 to 10 using a while loop.

# Expected Output: Numbers from 1 to 10: 1 2 3 4 5 6 7 8 9 10
# i=1
# while i <=10:
#     print(i,end=" ")
#     i=i+1

# b) Implement a program to calculate the sum of numbers from 1 to a user-provided limit using a while loop.
# num=10
# i=1
# sum=0
# while i<=num:
#     sum=sum+i
#     i=i+1
# print(sum)

# Input for sum calculation: 5
# Expected Output: The sum of numbers from 1 to 5 is 15

# Do-While Loop (Simulated using a While Loop):
# a) Write a program to repeatedly ask the user for input until they enter 'q'.
while True:
    variable=input("enter a variable")
    if variable=="q":
        break



# Input for 'q' simulation: 'a', 'b', 'q'
# Expected Output: The program repeatedly asks for input until 'q' is entered.


# b) Implement a program to simulate a dice roll and ask the user if they want to roll again.

# Input for dice roll simulation: 'y', 'n'
# Expected Output: The program simulates dice roll and asks if the user wants to roll again.


