# Roger Guo
# CMSC 210
# Homework Assignment #6
# IHRTLUHC
# To find out what number "one" has but "two" doesn't and store them in "diff"

# read the files
one = open("one.txt")
two = open("two.txt")
diff = open("diff.txt", "w")

# creating empty lists
listOne = []
listTwo = []
listDiff = []

# input the files into the lists
for line in one.readlines():
    listOne.append(int(line))

for line in two.readlines():
    listTwo.append(int(line))
switch = 1

# compare the two lists
for value1 in listOne:
    for value2 in listTwo:
        if value1 == value2:
            switch = 0
    if switch == 1:
        listDiff.append(value1)
    switch = 1

for value in listDiff:
    print(value)
    diff.write("{:3d}\n".format(value))

one.close()
two.close()
diff.close()