# Roger Guo
# CMSC 210
# Homework Assignment #4
# IHRTLUHC
# Program to find the roots of f(x)=ln(x) by Newton's method

import math

# Let the user input the value for x
# Let the user input a guess for the root
x = float(input("Enter the value for x: "))
t = float(input("Enter a guess for the root: "))

# Define the function and its derivative
def f(t):
    """defining the function in another form: f(t) = x - e^t"""
    return (x - math.e ** t)
def fp(t):
    """defining the derivative of the function"""
    return ((-1) * math.e ** t)

# Start applying Newton's method
y = f(t)
tolerance = 10 ** (-6)
while(y < -tolerance or y > tolerance):
    yp = fp(t)
    t = t - y/yp
    y = f(t)

print("Our root estimate result is " + str(t))
print("The actual root would be " + str(math.log(x)))