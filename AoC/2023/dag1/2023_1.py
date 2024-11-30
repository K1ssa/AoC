file = open('dag1.txt', "r")
data = file.read().strip()
total1 = 0
total2 = 0
for line in data.split('\n'):
    digit = []
    for i,x in enumerate(line):
        if x.isdigit():
            digit.append(x)
            # print(digit)
    digits = int(digit[0]+digit[-1])
    total1 += digits
print(total1)

for line in data.split('\n'):
    digit2 = []
    for i,x in enumerate(line):
        if x.isdigit():
            digit2.append(x)
        for z,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                digit2.append(str(z+1))
    digits2 = int(digit2[0]+digit2[-1])
    total2 += digits2
print(total2)

################Martin
# import re
#
# file = open("D:\\advent01.txt", "r")
# total = 0
# for line in file:
#     match = str.strip(re.sub(r'[a-z]', '', line, flags=re.IGNORECASE))
#     s1 = match[0]
#     s2 = match[-1]
#     s = s1 + s2
#     print(s)
#     total += int(s)
#
# print(total)
# file.close()
#
# import re
#
# file = open("D:\\advent01.txt", "r")
# total = 0
# for line in file:
#     rep = [("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5"), ("six", "6"), ("seven", "7"),
#         ("eight", "8"), ("nine", "9"), ("zero", "0")]
#     for old, new in rep:
#         line = line.replace(old, new)
#     match = str.strip(re.sub(r'[a-z]', '', line, flags=re.IGNORECASE))
#     s1 = match[0]
#     s2 = match[-1]
#     s = s1 + s2
#     total += int(s)
#
# print(total)
# file.close()