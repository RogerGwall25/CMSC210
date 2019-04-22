# Roger Guo
# CMSC 210
# Homework Assignment #5
# IHRTLUHC
# Redoing assignment #2 using tuples

# constructing the list
x = [1935,1940,1945,1950,1955,1960,1965,1970,1975,1980]
y = [32.1,30.5,24.4,23,19.1,15.6,12.4,9.7,8.9,7.2]
data = list(zip(x,y))

# Compute averages of the two data sets
count = 0
yearSum = 0
for year,pop in data:
    count += 1
    yearSum += year
    popSum = 0
for year,pop in data:
    popSum += pop
yearBar = yearSum / count
popBar = popSum / count

# Compute the variance and the covariance
covariance = 0
variance = 0
for pair in data:
    covariance += (pair[0] - yearBar) * (pair[1] - popBar)
    variance += (pair[0] - yearBar) ** 2

# Compute the coefficients of the regression line
beta = covariance / variance
alpha = popBar - beta * yearBar

# Getting the SSE of the computed regression line
SSE = 0
for pair in data:
    SSE = SSE + (alpha + beta * pair[0] - pair[1]) ** 2

# Extract the values of residuals
Residuals = []
for pair in data:
    Residuals.append(pair[1] - alpha - beta * pair[0])

# printing the table of residuals for the computed regression line
print("\n Table of Residuals")
for r in Residuals:
    print(" {:<5.2f}".format(r))

# printing the result of SSE
print("\n SSE = ", SSE)