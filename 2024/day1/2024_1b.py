from collections import Counter

a, b = [], []

with open('day1.txt', "r") as f:
    for line in f.readlines():
        x, y = (int(i) for i in line.split())
        a.append(x)
        b.append(y)
a.sort()
b.sort()

k = len(a)

h = Counter(b)
print(h)

print(sum(a[i]*h[a[i]] for i in range(k)))