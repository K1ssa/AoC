with open('day3.txt' , "r") as f:
    moves = f.readline().strip()

pos = (0, 0)
visited = set()
visited.add(pos)

for move in moves:
    x, y = pos
    if move == '>':
        x += 1
    elif move == '<':
        x -= 1
    elif move == 'v':
        y += 1
    elif move == '^':
        y -= 1
    pos = (x, y)
    visited.add(pos)

print(len(visited))



