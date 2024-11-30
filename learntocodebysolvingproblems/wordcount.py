apple_points = 0
banana_points = 0
apple_points= apple_points + (int(input('A3')*3))
banana_points= banana_points + (int(input('B3')*3))

apple_points= apple_points + (int(input('A2')*2))
banana_points= banana_points + (int(input('B2')*2))

apple_points= apple_points + (int(input('A1')*1))
banana_points= banana_points + (int(input('B1')*1))

if apple_points > banana_points:
    print('A won')
if banana_points > apple_points:
    print('B won')
if banana_points == apple_points:
    print('It is a tie')






# pi = 3.141592653589793
# radius = int(input())
# height = int(input())
# volume = (pi*radius**2*height)/3
# print(volume)