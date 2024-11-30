from itertools import permutations

permutations('0123456789abcdef', 4)
for i in permutations('0123456789abcdef', 4):
    print("".join(i))