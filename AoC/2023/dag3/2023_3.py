file = open('testdag3.txt', "r")

# data = []
# print(type(data))
data = [file.read().strip()]
# data = []
print(data)
print(type(data))

# s = set()
# with open('testdag3.txt', "r") as f:
#     # store the file content in 2d array
#     lines = [x.strip() for x in f.readlines()]
#
#     for row, line in enumerate(lines):
#         for col, char in enumerate(line):
#             if char.isdigit() or char == ".":
#                 continue
#
#             for x in [row - 1, row, row + 1]:
#                 for y in [col - 1, col, col + 1]:
#                     if x < 0 or x >= len(lines) or y < 0 or y >= len(lines[x]) or not lines[x][y].isdigit():
#                         continue
#                     while y > 0 and lines[x][y - 1].isdigit():
#                         y -= 1
#                     s.add((x, y))
#
# nums = []
#
# for x, y in s:
#     a = ""
#     while y < len(lines[x]) and lines[x][y].isdigit():
#         a += lines[x][y]
#         y += 1
#     nums.append(int(a))
#
# print(sum(nums))






#
# def calculate_sum_of_part_numbers(engine):
#     total_sum = 0
#     rows, cols = len(engine), len(engine[0])
#
#     for row in range(rows):
#         for col in range(cols):
#             if engine[row][col].isdigit():
#                 current_number = ""
#
#                 for i in range(row - 1, row + 2):
#                     for j in range(col - 1, col + 2):
#                         if 0 <= i < rows and 0 <= j < cols and engine[i][j] in '*+#$':
#                             current_number += engine[row][col]
#                             break
#
#                 if current_number:
#                     total_sum += int(current_number)
#
#     return total_sum
#
#
# # Example engine schematic
# engine_schematic = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "......#...",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598.."
# ]
#
# # Calculate the sum of part numbers
# result = calculate_sum_of_part_numbers(engine_schematic)
# print("Sum of part numbers:", result)
######################################################################
# def is_digit(b):
#     return b.isdigit()
#
# class Point:
#     def __init__(self, y, x):
#         self.y = y
#         self.x = x
#
# def main():
#     with open("testdag3.txt", "r") as file:
#         lines = file.read().splitlines()
#
#     ygrid = len(lines)
#     xgrid = len(lines[0])
#
#     grid = [[0] * xgrid for _ in range(ygrid)]
#     for y, line in enumerate(lines):
#         for x, char in enumerate(line):
#             grid[y][x] = char
#
#     neighbors = [(-1, -1), (0, -1), (1, -1),
#                  (-1, 0), (0, 0), (1, 0),
#                  (-1, 1), (0, 1), (1, 1)]
#
#     gears = {}
#     sum_ = 0
#     for y in range(ygrid):
#         for x in range(xgrid):
#             num = 0
#             has_symbol = False
#             is_gear = False
#             gear_coord = None
#             while is_digit(grid[y][x]):
#                 num = num * 10 + int(grid[y][x])
#                 for n in neighbors:
#                     if 0 <= y + n[1] < ygrid and 0 <= x + n[0] < xgrid:
#                         v = grid[y + n[1]][x + n[0]]
#                         if not is_digit(v) and v != '.':
#                             if v == '*':
#                                 is_gear = True
#                                 gear_coord = Point(x + n[0], y + n[1])
#                             has_symbol = True
#                 x += 1
#                 if x >= xgrid:
#                     break
#
#             if num > 0 and has_symbol:
#                 if is_gear:
#                     gears.setdefault(gear_coord, []).append(num)
#                 sum_ += num
#
#     print("Part 1:", sum_)  # 498559
#
#     sum_ = 0
#     for v in gears.values():
#         if len(v) == 2:
#             sum_ += v[0] * v[1]
#
#     print("Part 2:", sum_)  # 72246648
#
# if __name__ == "__main__":
#     main()
