# Roger Guo
# CMSC210 Midterm#1
# Problem#3
# IHRTLUHC
# 4/19/2019

# Constructing the list
A = [4, 15, 12, 5, 7, 15, 10, 5, 13, 8, 5, 7, 8, 1, 12, 7, 13, 12, 8]

# filter out the repeating ones
B = []
times = 0
for value in A:
    for value2 in B:
        if (value == value2):
            times = 1
    if (times == 0):
        B.append(value)
    times = 0

# sort the list and print it
B.sort()
for value in B:
    print(value)
