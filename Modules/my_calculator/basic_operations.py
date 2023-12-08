# my_calculator/basic_operations.py
from math_operations import add, subtract, multiply, divide

def square(x):
    """Square operation."""
    return multiply(x, x)

def cube(x):
    """Cube operation."""
    return multiply(x, multiply(x, x))
