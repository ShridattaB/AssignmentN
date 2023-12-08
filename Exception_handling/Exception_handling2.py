
try:
    num1=int(input("Enter a num1- "))
    num2=int(input("Enter a num2- "))
    result= num1/num2
    print(result)
except ValueError as vlu:
    print("value error")

except ZeroDivisionError as zr:
    print("not able to divided by 0")
else:
    print(result)

finally:
    print("code excution done")