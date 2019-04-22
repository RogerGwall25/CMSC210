# Roger Guo
# CMSC 210
# Homework Assignment #1
# IHRTLUHC
# An alternative way to fit a quadratic polynomial to a set of three data points (using two linear interpolations)

# The initial set of data points
x0 = 1.04
y0 = 2.71
x1 = 1.51
y1 = 2.55
x2 = 1.83
y2 = 2.82

# To construct the equation of a line that passes through (x0, y0) and (x1, y1)
# we use point slope form of linear function
m01 = (y1 - y0)/(x1 - x0)  # where m01 represents the slope of the line passes through (x0, y0) and (x1, y1)

# For the line passes through (x1, y1), (x2, y2), we do the same thing
m12 = (y2 - y1)/(x2 - x1)  # same as above

# Since we already have the point slope form of the equations of the two line
# we can estimate for y(1.7)
x = 1.7
y01 = y0 + m01 * (x - x0)
y12 = y1 + m12 * (x - x1)

# Finally we display the result
print("Using line that passes through (x0, y0) and (x1, y1), at x = 1.7, y is approximately =", y01)
print("Using line that passes through (x1, y1) and (x2, y2), at x = 1.7, y is approximately =", y12)