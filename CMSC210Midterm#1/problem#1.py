# Roger Guo
# CMSC210 Midterm#1
# Problem#1
# IHRTLUHC
# 4/19/2019

# Building the lists
x = [18.06, 15.57, 2.00, 1.27, 17.58, 17.19, 0.55, 6.03]
w = [-0.10, -0.20, -0.92, 0.31, 0.10, -0.54, 0.90, 0.88]
wSum = 0

# Computing the weighted sum
for i in range(0, len(x)):
    wSum = wSum + (w[i])*(x[i])

print(wSum)
