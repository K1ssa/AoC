with open('day3.txt', "r") as f:
    moves = f.readline().strip()

pos = [(0, 0), (0, 0)]
visited = set()
visited.add(pos[0])

i = 0
for move in moves:
    x, y = pos[i]
    if move == '>':
        x += 1
    elif move == '<':
        x -= 1
    elif move == 'v':
        y += 1
    elif move == '^':
        y -= 1
    pos[i] = (x, y)
    visited.add(pos[i])
    i = 1-i
print(visited)
print(len(visited))



