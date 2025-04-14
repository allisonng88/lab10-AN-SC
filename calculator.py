import math

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b): 
    return a + b
def sub(a, b):
    return b-a
def mul(a, b):
    return a*b

def div(a, b):
    try:
        if a!= 0:
            return b/a
        else:
            raise ZeroDivisionError
    except ZeroDivisionError:
        print(f"Error: Division by zero")


def log(a,b):
    try:
        if b<=0 and a<=1:
            raise ValueError
        else:
            return math.log(b,a)
    except ValueError:
        print("Error: Negative/0/1 base or Negative/0 argument")
def exp(a,b):
    return a**b







