file = open('day1.txt', "r")
data = file.read()
floor = 0
count = 0
for x in data:
    if x == '(':
        floor += 1
        count += 1
    elif x == ')':
        floor -= 1
        count += 1




