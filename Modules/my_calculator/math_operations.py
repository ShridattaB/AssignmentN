   # math_operations.py

def add(x, y):
    """Addition operation."""
    return x + y

def subtract(x, y):
    """Subtraction operation."""
    return x - y

def multiply(x, y):
    """Multiplication operation."""
    return x * y

def divide(x, y):
    """Division operation."""
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"
       