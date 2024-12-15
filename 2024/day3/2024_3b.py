import re
mem = 0
with open('day3.txt', "r") as f:
    data = f.read()
    non_data = re.sub(r"don't\(\).*?do\(\)", '', data, flags=re.DOTALL)
    mul = re.findall(r'mul\((\d+),(\d+)\)', non_data)
for m in mul:
    mem += (int(m[0])*int(m[1]))
print(mem)
