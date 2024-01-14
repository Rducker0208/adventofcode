import pprint
from typing import List, Any

import aoc_lube

# INPUT = r""".|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|...."""

INPUT = aoc_lube.fetch(year=2023, day=16)

row = []
paths_taken = []
start_cords = []
final_list = []
position = None
x_cord = None
row_number = None

horizontal_rows = {}  # // y-cords
vertical_rows = {}  # // x-cords

paths_left = [(0, 0,  'east')]
visited_Locations = [(0, 0)]


for row_number, row in enumerate(INPUT.splitlines()):
    horizontal_rows[row_number] = list(row)

# print(horizontal_rows)


for x_cord in range(len(row)):
    x_characters = []
    for row in horizontal_rows.values():
        x_character = row[x_cord]
        x_characters.append(x_character)
    vertical_rows[x_cord] = x_characters

max_x = x_cord
max_y = row_number

for i in range(len(vertical_rows)):
    start_cords.append((i, 0, 'south'))
    start_cords.append((i, max_y, 'north'))

for i in range(len(horizontal_rows)):
    start_cords.append((0, i, 'east'))
    start_cords.append((max_x, i, 'west'))


for start_pos in start_cords:
    start_cords.remove(start_pos)
    print(start_cords)
    print(start_pos)
    paths_left = [start_pos]
    paths_taken = []
    visited_Locations = []

    for path in paths_left:
        path_walked = []
        if path in paths_taken:
            continue

        # print(f'now following: {path}')

        paths_taken.append(path)

        x_cord = path[0]
        y_cord = path[1]
        direction = path[2]

        position = (x_cord, y_cord)
        path_walked.append((position, direction))

        while True:
            if x_cord < 0 or y_cord < 0:
                break
            position = (x_cord, y_cord)
            try:
                current_character = horizontal_rows[y_cord][x_cord]
            except KeyError:
                break
            except IndexError:
                break

            # vind nieuwe directie
            if direction == 'north':
                if current_character in ['.', '|']:
                    pass
                elif current_character == '\\':
                    direction = 'west'
                elif current_character == '/':
                    direction = 'east'
                elif current_character == '-':
                    paths_left.append((x_cord, y_cord, 'west'))
                    paths_left.append((x_cord, y_cord, 'east'))
                    break

            elif direction == 'east':
                # print(current_character)
                if current_character in ['.', '-']:
                    pass
                elif current_character == '\\':
                    direction = 'south'
                elif current_character == '/':
                    direction = 'north'
                elif current_character == '|':
                    paths_left.append((x_cord, y_cord, 'north'))
                    paths_left.append((x_cord, y_cord, 'south'))
                    break

            elif direction == 'south':
                if current_character in ['.', '|']:
                    pass
                elif current_character == '\\':
                    direction = 'east'
                elif current_character == '/':
                    direction = 'west'
                elif current_character == '-':
                    paths_left.append((x_cord, y_cord, 'west'))
                    paths_left.append((x_cord, y_cord, 'east'))
                    break

            elif direction == 'west':
                if current_character in ['.', '-']:
                    pass
                elif current_character == '\\':
                    direction = 'north'
                elif current_character == '/':
                    direction = 'south'
                elif current_character == '|':
                    paths_left.append((x_cord, y_cord, 'north'))
                    paths_left.append((x_cord, y_cord, 'south'))
                    break

            if position not in visited_Locations:
                visited_Locations.append(position)

            path_walked.append((position, direction))

            # // vind nieuwe locatie
            if direction == 'north':
                y_cord -= 1
            elif direction == 'east':
                x_cord += 1
            elif direction == 'south':
                y_cord += 1
            elif direction == 'west':
                x_cord -= 1

    # print(len(visited_Locations))
    final_list.append(len(visited_Locations))

print(final_list)
print(max(final_list))