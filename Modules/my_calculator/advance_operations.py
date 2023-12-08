from basic_operations import square, cube,multiply

def exponentiation(x, n):
    """Exponentiation operation."""
    result = 1
    for _ in range(n):
        result = multiply(result, x)
    return result

def square_root(x):
    """Square root operation."""
    return x ** 0.5
