paper = 0
ribbon = 0

with open('day2.txt', "r") as f:
    for line in f.readlines():
        edges = [int(z) for z in line.strip().split('x')]
        sides = [edges[0]*edges[1], edges[1]*edges[2], edges[2]*edges[0]]
        smallest_side = min(sides)
        paper += 2*(sum(sides))+smallest_side

        dist = 2*(edges[0]+edges[1])
        bow = edges[0]*edges[1]*edges[2]
        ribbon += dist+bow
print(paper)
print(ribbon)