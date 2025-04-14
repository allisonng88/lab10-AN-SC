"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math
def square_root(a):
    try:
        if a >= 0:
            return math.sqrt(a)
        else:
            raise ValueError
    except ValueError:
        print("Value Error")
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b
def sub(a, b):
    return b-a
def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        if a != 0:
            return b/a
        else:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print(f"Division by zero error")
def logarithm(a, b):
    try:
        if a > 1 or b > 0:
            return math.log(b, a)
        else:
            raise ValueError
    except ZeroDivisionError:
        print(f"Value Error")
def exponent(a, b):
    return a**b








