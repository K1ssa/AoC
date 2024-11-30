from collections import defaultdict
file = open('day2.txt', "r")
data = file.read().strip()
legal = 0
max_color = {'red': 12, 'green': 13, 'blue': 14}
for line in data.split('\n'):
    ok = True
    id, line = line.split(':')
    for game in line.split(';'):
        for turn in game.split(','):
            amount, color = turn.split()
            if int(amount) > max_color.get(color, 0):
                ok = False
    if ok:
        legal += int(id.split()[-1])
print(legal)

legal2 = 0
for line in data.split('\n'):
    id, line = line.split(':')
    min_dict = defaultdict(int)
    for game in line.split(';'):
        for turn in game.split(','):
            amount, color = turn.split()
            amount = int(amount)
            min_dict[color] = max(min_dict[color], amount)
    count = 1
    for x in min_dict.values():
        count *= x
    legal2 += count
print(legal2)
