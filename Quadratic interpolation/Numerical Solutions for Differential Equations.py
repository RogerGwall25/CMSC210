# Roger Guo
# CMSC 210
# Homework Assignment #3
# IHRTLUHC
# Numerical Solutions for Differential Equations

import math

# let the user input the number of steps N to take
# Define variables
N = int(input('Enter N: '))
h = 1/N
x = 0.5
t = 0
step = 0

# main loop for approximating the points and displaying results
print("t           x(estimated)      x(actual)")
while(step < N):
    print('{:<2.2f}        {:<2.7f}         {:<2.7f}'.format(t,x,(2 - (3/2) * (math.e ** t) + 2 * t + t * t)))
    k1 = x - t * t
    k2 = x + k1 * h / 2 - (t + h / 2) * (t + h / 2)
    k3 = x + k2 * h / 2 - (t + h / 2) * (t + h / 2)
    k4 = x + k3 * h - (t + h) * (t + h)
    x = x + (k1 + k2 * 2 + k3 * 2 + k4) * h / 6
    t = t + h
    step = step + 1
print('{:<2.2f}        {:<2.7f}         {:<2.7f}'.format(t,x,(2 - (3/2) * (math.e ** t) + 2 * t + t * t)))