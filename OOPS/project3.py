# write a program to print list of option as menu 
# take user input for menu option

# take 2 number input from user for operation 

# perform operation and print result again ask for menu choise 
# if user enter 5 then exit

# -Input Output

# MENU:

# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit

# Enter the operation you wish to perform:1
# Enter First number :5
# Enter Second number:10
# Result: 5 + 10 = 15

# Enter the operation you wish to perform:2
# Enter First number :10
# Enter Second number:6
# Result: 10 - 6 = 4

# Enter the operation you wish to perform:3
# Enter First number :4
# Enter Second number:4
# Result: 4 * 4 = 16

# Enter the operation you wish to perform:4
# Enter First number :10
# Enter Second number:2
# Result: 10 / 2 = 5

# Enter the operation you wish to perform:6
# > Invalid Input

# Enter the operation you wish to perform:5
# BYE!!!

print("MENU:")

while True:
    print('''1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit''')
    choice=int(input("Enter the operation you wish to perform:"))
    if choice==1:
        num1=int(input("Enter First number :"))
        num2=int(input("Enter Second number:"))
        ans=num1+num2
        print(f"Result: {num1}+{num2}  = {ans}")

    if choice==2:
        num1=int(input("Enter First number :"))
        num2=int(input("Enter Second number:"))
        ans=num1-num2
        print(f"Result: {num1}-{num2}  = {ans}")

    if choice==3:
        num1=int(input("Enter First number :"))
        num2=int(input("Enter Second number:"))
        ans=num1*num2
        print(f"Result: {num1}*{num2}  = {ans}")

    if choice==4:
        num1=int(input("Enter First number :"))
        num2=int(input("Enter Second number:"))
        ans=num1/num2
        print(f"Result: {num1}/{num2}  = {ans}")
    
    if choice==5:
        break
    else:
        print("Invalid input")





    


    




