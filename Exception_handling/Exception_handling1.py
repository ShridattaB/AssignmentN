# try:
#     x = int(input("Enter a number: "))
#     result = 10 / x
#     print("Result:", result)
# except ValueError:
#     print("Invalid input. Please enter a valid number.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# else:
#     print("No exceptions occurred.")
# finally:
#     print("This will always be executed.")

try:
    # Code that might raise an exception
    result = 10 / 2
    print("Result:", result)

finally:
    # Code that always runs, regardless of exceptions
    print("This will always execute.")
