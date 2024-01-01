import pprint
import aoc_lube

# INPUT = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""

INPUT = aoc_lube.fetch(year=2023, day=14)

round_stone_locations = []
cycle_list = []
test_list = []
cube_stone_locations = []
cycles_left = 1000000000

rows = {}
result_dict = {}
cords_to_number_loc = {}
cycle_count = 1
counter = 1

input_length = len(INPUT.splitlines())

# creer dictionary met rows en hun ids
for row in INPUT.splitlines():
    rows[input_length] = row
    input_length -= 1


# verzamel coordinaten van beide soorten stenen
for y, row in rows.items():
    for x, character in enumerate(row):
        if character == '#':
            cube_stone_locations.append((x, y))
        elif character == 'O':
            round_stone_locations.append((x, y))


print(round_stone_locations)


def north(original_x, original_y):
    global round_stone_locations
    x_to_check = original_x
    y_to_check = original_y + 1
    found_new_loc = False

    while not y_to_check > len(INPUT.splitlines()):

        # verzamwl item om naar te kjken
        character_to_check = (original_x, y_to_check)

        # check wat dit item is
        if character_to_check in round_stone_locations or character_to_check in cube_stone_locations:
            highest_cords = (original_x, y_to_check - 1)
            round_stone_locations.append(highest_cords)
            round_stone_locations.remove((original_x, original_y))
            found_new_loc = True
            break
        y_to_check += 1

    if found_new_loc is False:
        round_stone_locations.append((original_x, len(INPUT.splitlines())))
        round_stone_locations.remove((original_x, original_y))

    return round_stone_locations


def west(original_x, original_y):
    global round_stone_locations
    x_to_check = original_x - 1
    y_to_check = original_y
    found_new_loc = False

    while x_to_check > -1:
        character_to_check = (x_to_check, original_y)
        if character_to_check in round_stone_locations or character_to_check in cube_stone_locations:
            highest_cords = (x_to_check + 1, original_y)
            round_stone_locations.append(highest_cords)
            # print(f'added: {highest_cords} to list')
            round_stone_locations.remove((original_x, original_y))
            found_new_loc = True
            break

        x_to_check -= 1

    if found_new_loc is False:
        round_stone_locations.append((0, original_y))
        # print(f'false: {(original_x, original_y)}, added {(0, original_y)} to list')
        round_stone_locations.remove((original_x, original_y))

    return round_stone_locations


def east(original_x, original_y):
    global round_stone_locations
    x_to_check = original_x + 1
    y_to_check = original_y
    found_new_loc = False
    # print(f'len: {len(INPUT.splitlines()[0])}')
    # print(f'original x: {original_x}')
    # print(f'x: {x_to_check}')
    # print(f'original y: {original_y}')
    # print(f'y: {y_to_check}')

    while not x_to_check == len(INPUT.splitlines()[0]):
        # print(x_to_check)
        character_to_check = (x_to_check, original_y)
        if character_to_check in round_stone_locations or character_to_check in cube_stone_locations:
            highest_cords = (x_to_check - 1, original_y)
            round_stone_locations.append(highest_cords)
            # print(f'added: {highest_cords} to list')
            round_stone_locations.remove((original_x, original_y))
            found_new_loc = True
            break

        x_to_check += 1

    if found_new_loc is False:
        round_stone_locations.append((len(INPUT.splitlines()) - 1, original_y))
        # print(f'false: {(original_x, original_y)}, added {(len(INPUT.splitlines()) - 1, original_y)} to list')
        round_stone_locations.remove((original_x, original_y))

    return round_stone_locations


def south(original_x, original_y):
    global round_stone_locations
    x_to_check = original_x
    y_to_check = original_y - 1
    found_new_loc = False

    while y_to_check > 0:

        # verzamel item om naar te kjken
        character_to_check = (original_x, y_to_check)
        if character_to_check in round_stone_locations or character_to_check in cube_stone_locations:
            highest_cords = (original_x, y_to_check + 1)
            round_stone_locations.append(highest_cords)
            # print(f'added: {highest_cords} to list')
            round_stone_locations.remove((original_x, original_y))
            found_new_loc = True
            break

        y_to_check -= 1

    if found_new_loc is False:
        # print(f'false: {(original_x, 1)}')
        round_stone_locations.append((original_x, 1))
        round_stone_locations.remove((original_x, original_y))
    return round_stone_locations


while cycles_left > 0:

    # noord
    for y, row in rows.items():
        for x, character in enumerate(row):
            cords = (x, y)
            if cords in round_stone_locations:
                round_stone_locations = north(x, y)
    # print(round_stone_locations)

    # west
    for y, row in rows.items():
        for x, character in enumerate(row):
            cords = (x, y)
            if cords in round_stone_locations:
                round_stone_locations = west(x, y)
    # print(round_stone_locations)

    # south
    sorted_list = []
    for item in rows.keys():
        sorted_list.append(item)
    sorted_list.sort()

    for y in sorted_list:
        row = rows[y]
        for x, character in enumerate(row):
            cords = (x, y)
            if cords in round_stone_locations:
                round_stone_locations = south(x, y)

    # east
    cords_list = []
    for y, row in rows.items():
        for x, character in enumerate(row):
            cords = (x, y)
            if cords in round_stone_locations:
                cords_list.append(cords)
    cords_list.reverse()

    for cords in cords_list:
        if cords in round_stone_locations:
            # print(cords)
            round_stone_locations = east(cords[0], cords[1])

    print(round_stone_locations)
    list_copy = round_stone_locations.copy()
    if list_copy in result_dict.values():
        print('_________found match at:___________')
        print(list_copy)
        cycle = cords_to_number_loc[str(list_copy)]
        print(f'At cycle {cycle} and {counter}')
        break
    result_dict[counter] = list_copy
    cords_to_number_loc[str(list_copy)] = counter
    counter += 1
    cycles_left -= 1


# for location_number, location_list in result_dict.items():
#     total = 0
#     for location in location_list:
#         total += location[1]
#     print(f'Location number: {location_number}\n'
#           f'total: {total}')

cycle_length = counter - cycle
ofset = cycle - 1
print(cycle_length)

where_in_the_cycle = (1000000000 - ofset) % cycle_length + ofset
print(where_in_the_cycle)
location_to_check = result_dict[where_in_the_cycle]
print(location_to_check)

total = 0
for location in location_to_check:
    total += location[1]

print(total)

# noord:
# [(0, 10), (0, 9), (2, 10), (3, 10), (0, 8), (1, 10), (4, 8), (9, 8), (1, 9), (7, 10), (0, 7), (5, 7), (2, 4), (6, 7), (9, 4), (7, 4), (1, 8), (2, 3)]

# south:
# [(1, 1), (2, 1), (7, 3), (2, 2), (6, 3), (9, 1), (0, 3), (5, 5), (1, 2), (7, 6), (0, 4), (1, 3), (4, 1), (9, 6), (0, 5), (2, 6), (3, 8), (0, 6)]

# east:
# [(4, 1), (3, 1), (9, 3), (9, 4), (8, 4), (4, 4), (6, 5), (1, 5), (7, 6), (6, 6), (9, 7), (8, 7), (2, 7), (1, 7), (3, 9), (2, 9), (1, 9), (4, 10)]

# west
# [(0, 10), (0, 9), (1, 9), (2, 9), (0, 7), (1, 7), (4, 7), (5, 7), (0, 6), (1, 6), (0, 5), (3, 5), (0, 4), (6, 4), (7, 4), (0, 3), (1, 1), (2, 1)]

# 1
# [[(4, 1), (3, 1), (4, 2), (9, 3), (8, 3), (7, 3), (6, 3), (4, 4), (6, 5), (1, 5), (7, 6), (6, 6), (5, 6), (2, 7), (1, 7), (4, 8), (3, 8), (8, 9)]]

# 3
# [(9, 1), (4, 1), (3, 1), (2, 1), (9, 2), (4, 2), (9, 3), (8, 3), (7, 3), (9, 4), (4, 4), (6, 5), (1, 5), (7, 6), (6, 6), (5, 6), (2, 7), (8, 9)]

# 10
# [(9, 1), (4, 1), (3, 1), (2, 1), (9, 2), (4, 2), (9, 3), (8, 3), (7, 3), (9, 4), (4, 4), (6, 5), (1, 5), (7, 6), (6, 6), (5, 6), (2, 7), (8, 9)]
