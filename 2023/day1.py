file = open('day1.txt', "r")
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
