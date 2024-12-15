import re
mem = 0
with open('day3.txt', "r") as f:
    for line  in f.readlines():
        mul = re.findall(r'mul\((\d+),(\d+)\)', line)
        for m in mul:
            mem += (int(m[0])*int(m[1]))
print(mem)
