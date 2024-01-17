# WARNING: very slow
INPUT = open('main.txt').read()

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


def north(original_x, original_y):
    global round_stone_locations
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
    found_new_loc = False

    while x_to_check > -1:
        character_to_check = (x_to_check, original_y)
        if character_to_check in round_stone_locations or character_to_check in cube_stone_locations:
            highest_cords = (x_to_check + 1, original_y)
            round_stone_locations.append(highest_cords)
            round_stone_locations.remove((original_x, original_y))
            found_new_loc = True
            break

        x_to_check -= 1

    if found_new_loc is False:
        round_stone_locations.append((0, original_y))
        round_stone_locations.remove((original_x, original_y))

    return round_stone_locations


def east(original_x, original_y):
    global round_stone_locations
    x_to_check = original_x + 1
    found_new_loc = False

    while not x_to_check == len(INPUT.splitlines()[0]):
        character_to_check = (x_to_check, original_y)
        if character_to_check in round_stone_locations or character_to_check in cube_stone_locations:
            highest_cords = (x_to_check - 1, original_y)
            round_stone_locations.append(highest_cords)
            round_stone_locations.remove((original_x, original_y))
            found_new_loc = True
            break

        x_to_check += 1

    if found_new_loc is False:
        round_stone_locations.append((len(INPUT.splitlines()) - 1, original_y))
        round_stone_locations.remove((original_x, original_y))

    return round_stone_locations


def south(original_x, original_y):
    global round_stone_locations
    y_to_check = original_y - 1
    found_new_loc = False

    while y_to_check > 0:

        # verzamel item om naar te kjken
        character_to_check = (original_x, y_to_check)
        if character_to_check in round_stone_locations or character_to_check in cube_stone_locations:
            highest_cords = (original_x, y_to_check + 1)
            round_stone_locations.append(highest_cords)
            round_stone_locations.remove((original_x, original_y))
            found_new_loc = True
            break

        y_to_check -= 1

    if found_new_loc is False:
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

    # west
    for y, row in rows.items():
        for x, character in enumerate(row):
            cords = (x, y)
            if cords in round_stone_locations:
                round_stone_locations = west(x, y)

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
            round_stone_locations = east(cords[0], cords[1])

    list_copy = round_stone_locations.copy()
    if list_copy in result_dict.values():
        cycle = cords_to_number_loc[str(list_copy)]
        break
    result_dict[counter] = list_copy
    cords_to_number_loc[str(list_copy)] = counter
    counter += 1
    cycles_left -= 1


cycle_length = counter - cycle
ofset = cycle - 1


where_in_the_cycle = (1000000000 - ofset) % cycle_length + ofset
location_to_check = result_dict[where_in_the_cycle]

total = 0
for location in location_to_check:
    total += location[1]

print(total)