"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b
def sub(a, b):
    return b-a
def multiply(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a
try:
    a = int(input("a: "))
    b = int(input("b: "))
    result = divide(a, b)
except ZeroDivisionError:
    print(f"Division by zero error")
def logarithm(a, b):
    if b <= 0 or a <= 1:
        raise ValueError
    return math.log(b, a)
try:
    a = int(input("a: "))
    b = int(input("b: "))
    result = logarithm(a, b)
except ValueError:
    print(f"Value Error")
def exponent(a, b):
    return a**b








