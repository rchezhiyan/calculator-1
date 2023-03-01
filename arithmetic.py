"""Functions for common math operations."""


def add(num1, num2):
    """Return the sum of num1 and num2."""
    ans = num1 + num2
    return ans


def subtract(num1, num2):
    """Return the value of num1 minus num2."""
    ans = num1 - num2
    return ans


def multiply(num1, num2):
    """Multiply the num1 by num2 and return the result."""
    ans = num1 * num2
    return ans

def divide(num1, num2):
    """Divide the num1 by num2, returning a floating point."""
    ans = num1/num2
    return ans


def square(num1):
    """Return the square of num1."""
    ans = num1 * num1
    return ans

def cube(num1):
    """Return the cube of num1."""
    ans = num1*num1*num1
    return ans


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    ans = pow(num1, num2)
    return ans
    

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    ans = num1%num2
    return ans
