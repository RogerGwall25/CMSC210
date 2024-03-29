# Roger Guo
# CMSC 210
# Homework Assignment #2
# IHRTLUHC
# Printing a table (modified from the example from the lecture note)

# The data set for this example is farm population in the United States over several decades.
x = [1935, 1940, 1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980]
y = [32.1 ,30.5 ,24.4 ,23 ,19.1 ,15.6 ,12.4 ,9.7 ,8.9 ,7.2]

# Compute averages of the two data sets
count = 0
xSum = 0
for year in x:
    count += 1
    xSum += year
    ySum = 0
for pop in y:
    ySum += pop
    xBar = xSum / count
yBar = ySum / count

# Compute the variance and the covariance
covariance = 0
variance = 0
for i in range(0, count):
    covariance += (x[i] - xBar) * (y[i] - yBar)
    variance += (x[i] - xBar) ** 2
    
# Compute the coefficients of the regression line
    beta = covariance/variance
    alpha = yBar - beta * xBar
    
# Getting the SSE of the computed regression line
SSE = 0
for i in range(0, count):
    SSE = SSE + (alpha + beta * x[i] - y[i]) ** 2
    
# printing the table of residuals for the computed regression line
print("\n Table of Residuals")
for i in range(0, count):
        print(" {:<5.2f}".format(y[i] - alpha - beta * x[i]))

# printing the result of SSE
print("\n SSE = ",SSE)