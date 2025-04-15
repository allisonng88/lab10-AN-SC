# https://github.com/allisonng88/lab10-AN-SC
# Partner 1: Allison Ng
# Partner 2: Shivani Chandrasekar

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

# First example
import math
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
# add try and catch outside of function
def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b
def subtract(a, b):
    return b-a
def mul(a, b):
    return a * b
def div(a, b):
    if a != 0:
        return b/a
    else:
        raise ZeroDivisionError
def logarithm(a, b):
    if a > 1 or b > 0:
        return math.log(b, a)
    else:
        raise ValueError
def exp(a, b):
    return a**b








