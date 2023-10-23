# 2: Create a function that checks if a given number is even or odd and returns an       appropriate message.

#       Input: even_or_odd(2)
#       Expected Output: "Even"

def even_or_odd(a):
    if a%2==0:
        print("Even")
    else:
        print("odd")

even_or_odd(2)