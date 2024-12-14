safe = 0
report = []
with open('day2.txt', "r") as f:
    for s in f.readlines():
        report.append([int(i) for i in s.split()])
print(report)
for r in report:
    k = len(r)
    safe += ((all(1 <= r[i+1]-r[i] <= 3 for i in range(k-1)))
                or (all(1 <= r[i]-r[i+1] <= 3 for i in range(k-1))))
print(safe)