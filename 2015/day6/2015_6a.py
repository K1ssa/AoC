nice = 0

with open('day5.txt', "r") as f:
    for line in f.readlines():
        s = line.strip()
        req1 = sum(char in 'aeiou' for char in s) >= 3
        req2 = any(s[i] == s[i+1] for i in range(len(s)-1))
        req3 = not any(x in s for x in ['ab', 'cd', 'pq', 'xy'])
        nice += (req1 and req2 and req3)

print(nice)