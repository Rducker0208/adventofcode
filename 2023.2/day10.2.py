import pprint

import aoc_lube

# INPUT = """...........
# .S-------7.
# .|F-----7|.
# .||.....||.
# .||.....||.
# .|L-7.F-J|.
# .|..|.|..|.
# .L--J.L--J.
# ..........."""
# valid_input = [(2, 6), (3, 6), (7, 6), (8, 6)]

# INPUT = """.F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ..."""
# valid input: [(14, 3), (7, 4), (8, 4), (9, 4), (7, 5), (8, 5), (6, 6), (14, 6)]
#
# INPUT = """FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJIF7FJ-
# L---JF-JLJIIIIFJLJJ7
# |F|F-JF---7IIIL7L|7|
# |FFJF7L7F-JF7IIL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L"""
# valid_input = [(14, 3), (10, 4), (11, 4), (12, 4), (13, 4), (11, 5), (12, 5), (13, 5), (13, 6), (14, 6)]

INPUT = aoc_lube.fetch(year=2023, day=10)

row_dict = {}
loop_cords_list = []
possible_locations = []
new_results = []
going_down_chracters = ['F', '7']
going_up_characters = ['L', 'J']
tiles_in = 0
S_index = None
current_tile = None

# // verzamel row data en hun ids
for row_number, row in enumerate(INPUT.splitlines()):
    row_dict[row_number] = row

# print(row_dict)


# // vind startpunt oftewel de index van S
for row_number, row in row_dict.items():
    if 'S' in row:
        S_index = (row.index('S'), row_number)
        loop_cords_list.append(S_index)
        break

print(S_index)


# // zoek naar paden die langs de S liggen om te kijken welke kant je op kunt
def get_loop_start():
    S_x = S_index[0]
    S_y = S_index[1]

    # // pad begint rechts
    if row_dict[S_y][S_x + 1] in ['-', 'J', '7']:
        starting_point = (S_x + 1, S_y)
        loop_cords_list.append(starting_point)
        direction = 'right'
        # print('rechts')
        return starting_point, direction

    # // pad begint links
    elif row_dict[S_y][S_x - 1] in ['L', '-', 'F']:
        starting_point = (S_x - 1, S_y)
        loop_cords_list.append(starting_point)
        direction = 'left'
        # print('links')
        return starting_point, direction

    # // het pad begint boven
    elif row_dict[S_y - 1][S_x] in ['7', 'F', '|']:
        starting_point = (S_x, S_y - 1)
        loop_cords_list.append(starting_point)
        direction = 'up'
        # print('boven')
        return starting_point, direction

    # het pad begint benden
    elif row_dict[S_y + 1][S_x] in ['|', 'J', 'L']:
        starting_point = (S_x, S_y + 1)
        loop_cords_list.append(starting_point)
        direction = 'down'
        # print('benden')
        return starting_point, direction


current_location, current_direction = get_loop_start()
# print('___________________________________')
# print(current_location)
# print('___________________________________')


# // kijk welke kant je op moet om loop te volgen
def get_direction(original_direction, location_to_check):

    # print(location_to_check)
    new_direction = None
    if row_dict[location_to_check[1]][location_to_check[0]] == '|':
        if original_direction == 'down':
            new_direction = 'down'
        else:
            new_direction = 'up'

    elif row_dict[location_to_check[1]][location_to_check[0]] == 'L':
        if original_direction == 'down':
            new_direction = 'right'
        else:
            new_direction = 'up'

    elif row_dict[location_to_check[1]][location_to_check[0]] == '-':
        if original_direction == 'right':
            new_direction = 'right'
        else:
            new_direction = 'left'

    elif row_dict[location_to_check[1]][location_to_check[0]] == 'J':
        if original_direction == 'right':
            new_direction = 'up'
        else:
            new_direction = 'left'

    elif row_dict[location_to_check[1]][location_to_check[0]] == '7':
        if original_direction == 'up':
            new_direction = 'left'
        else:
            new_direction = 'down'

    elif row_dict[location_to_check[1]][location_to_check[0]] == 'F':
        if original_direction == 'up':
            new_direction = 'right'
        else:
            new_direction = 'down'

    else:
        new_direction = 'S'

    return new_direction


# loop door alle locaties om coordinaten van de loop te vinden
while True:
    # print(current_location)
    current_direction = get_direction(current_direction, current_location)
    if current_direction == 'S':
        break
    if current_direction == 'left':
        current_location = (current_location[0] - 1, current_location[1])
    elif current_direction == 'right':
        current_location = (current_location[0] + 1, current_location[1])
    elif current_direction == 'up':
        current_location = (current_location[0], current_location[1] - 1)
    elif current_direction == 'down':
        current_location = (current_location[0], current_location[1] + 1)
    # print(current_direction)
    # print(current_location)
    loop_cords_list.append(current_location)

# print('#######################')
# print(loop_cords_list)
# print('#######################')

# // verzamel alle mogelijke kandidtaten voor punten in de loop
for y_index, row in enumerate(INPUT.splitlines()):
    for x_index, location in enumerate(row):
        location_cords = (x_index, y_index)
        if location_cords in loop_cords_list:
            pass
        else:
            if y_index == 0 or y_index == max(row_dict.keys()) or x_index == 0 or x_index + 1 == len(row):
                pass
            else:
                possible_locations.append(location_cords)


# print(possible_locations)

# check voor horizontale overneekomsten
for location in possible_locations:
    x_cord = location[0]
    y_cord = location[1]

    interceptions = 0
    streak = False
    streak_start_char = None
    loop_valid = None
    loop = False

    while x_cord >= 0:
        location_to_check = (x_cord, y_cord)
        # print(location_to_check)
        if location_to_check in loop_cords_list:
            character = row_dict[y_cord][x_cord]
            # print('if')
            if character == '|':
                # print('pipe char')
                interceptions += 1
            else:
                # print('else 1')
                if loop is False:
                    streak_start_char = character
                    loop = True
                else:
                    if character == '-':
                        pass
                    else:
                        # print('else')
                        if streak_start_char in going_up_characters:
                            if character in going_up_characters:
                                loop_valid = False
                            elif character in going_down_chracters:
                                loop_valid = True
                        elif streak_start_char in going_down_chracters:
                            if character in going_down_chracters:
                                loop_valid = False
                            elif character in going_up_characters:
                                loop_valid = True

            if loop_valid is True:
                # print(f'Found loop:'
                #       f'from: {streak_start_char}'
                #       f'To: {character}')
                interceptions += 1
                loop_valid = None
                loop = False

            elif loop_valid is False:
                loop_valid = None
                loop = False
                # print(f'cancled loop:\n'
                #       f'    from: {streak_start_char}\n'
                #       f'    To: {character}')
        # print(f'{location}: {character}')
        x_cord -= 1

    # print(f'Location: {location}'
    #       f'Interceptions: {interceptions}')

    if interceptions % 2 != 0 and interceptions != 0:
        new_results.append(location)


print(new_results)
print(len(new_results))