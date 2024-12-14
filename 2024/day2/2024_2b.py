safe = 0
report = []
with open('day2.txt', "r") as f:
    for s in f.readlines():
        report.append([int(i) for i in s.split()])
print(report)
def is_save(v):
    k = len(v)
    return ((all(1 <= v[i + 1] - v[i] <= 3 for i in range(k - 1)))
             or (all(1 <= v[i] - v[i + 1] <= 3 for i in range(k - 1))))

for r in report:
    safe += (is_save(r) or any(is_save(r[:i] + r[i+1:]) for i in range(len(r))))

print(safe)