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


horizontal_rows = {}  # // y-cords
vertical_rows = {}  # // x-cords

paths_left = [(0, 0,  'east')]
visited_Locations = [(0, 0)]

row = []
paths_taken = []
position = None

for row_number, row in enumerate(INPUT.splitlines()):
    horizontal_rows[row_number] = list(row)

print(horizontal_rows)


for x_cord in range(len(row)):
    x_characters = []
    for row in horizontal_rows.values():
        x_character = row[x_cord]
        x_characters.append(x_character)
    vertical_rows[x_cord] = x_characters


for path in paths_left:
    path_walked = []
    if path in paths_taken:
        continue

    print(f'now following: {path}')

    paths_taken.append(path)

    x_cord = path[0]
    y_cord = path[1]
    direction = path[2]

    position = (x_cord, y_cord)
    path_walked.append((position, direction))

    while True:
        print(position)
        if x_cord < 0 or y_cord < 0:
            break
        position = (x_cord, y_cord)
        try:
            current_character = horizontal_rows[y_cord][x_cord]
        except KeyError:
            break
        except IndexError:
            break

        print(current_character)
        print(direction)

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

    print(path_walked)
    # quit()/


print(visited_Locations)
print(len(visited_Locations))
