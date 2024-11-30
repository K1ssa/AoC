from collections import defaultdict
file = open('dag2.txt', "r")
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



# p1 = 0
# p2 = 0
# for line in data.split('\n'):
#     ok = True
#     id, line = line.split(':')
#     c = defaultdict(int)
#     for game in line.split(';'):
#         for turn in game.split(','):
#             amount, color = turn.split()
#             amount = int(amount)
#             c[color] = max(c[color], amount)
#             if int(amount) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
#                 ok = False
#         score = 1
#         for v in c.values():
#             score *= v
#         p2 += score
#         if ok:
#             p1 += int(id.split()[-1])
# print(p1)
# print('=' * 80)
# print(p2)
###########voorbeeld
# p1 = 0
# p2 = 0
# #only 12 red cubes, 13 green cubes, and 14 blue cubes?
# for line in data.split('\n'):
#   ok = True
#   id_, line = line.split(':')
#   V = defaultdict(int)
#   for event in line.split(';'):
#     for balls in event.split(','):
#       n,color = balls.split()
#       n = int(n)
#       V[color] = max(V[color], n)
#       if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
#         ok = False
#   score = 1
#   for v in V.values():
#     score *= v
#   p2 += score
#   if ok:
#     p1 += int(id_.split()[-1])
# print(p1)
# print(p2)