# Roger Guo
# CMSC210 Midterm#1
# Problem#2
# IHRTLUHC
# 4/19/2019

# Let the user input the two number
switch = 0
while (switch == 0):
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    if (x < 1 or y < 1):
        print("Come on...POSITIVE INTEGERS ONLY\n")
    else:
        switch = 1

# print("here we go")

# constructing the list of divisors for the two number
divisorsX = []
divisorsY = []

# adding divisors to the lists
d = 2
while x > 1:
    if x % d == 0:
        divisorsX.append(d)
        x = x//d
    else:
        # If d is not a divisor, move on to the next d to try.
        d += 1
d = 2
while y > 1:
    if y % d == 0:
        divisorsY.append(d)
        y = y//d
    else:
        # If d is not a divisor, move on to the next d to try.
        d += 1

# see if the two numbers have common factors
c = 0
for dX in divisorsX:
    for dY in divisorsY:
        if (dX == dY):
            c = 1

if (c == 1):
    print("Sorry but these two aren't relatively prime...")
else:
    print("These two are relatively prime!!!")
