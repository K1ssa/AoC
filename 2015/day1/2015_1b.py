
    # (()) and ()() both result in floor 0.
    # ((( and (()(()( both result in floor 3.
    # ))((((( also results in floor 3.
    # ()) and ))( both result in floor -1 (the first basement level).
    # ))) and )())()) both result in floor -3.




file = open('day1.txt', "r")
data = file.read()
floor = 0
count = 0
for x in data:
    if x == '(':
        floor += 1
        count += 1
    elif x == ')':
        floor -= 1
        count += 1

    if floor == -1:
        print(count)
        break



