nice = 0

with open('day5.txt', "r") as f:
    for line in f.readlines():
        s = line.strip()
        req1 = False
        for i in range(len(s)-1):
            pair = s[i:i+2]
            for j in range(i+2, len(s)-1):
                pair2 = s[j:j+2]
                if pair == pair2:
                    req1 = True
                    break
        req2 = any(s[i] == s[i+2] for i in range(len(s)-2))
        nice += (req1 and req2)

print(nice)

