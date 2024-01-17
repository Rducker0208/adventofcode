ROWS_og = open('main.txt').read().splitlines()

galaxy_cords = {}
path_distances = {}
galaxy_id = 1
x_axis = 0
total_sum = 0


def expand_galaxy(original_galaxy):
    added_new = False
    row = None

    rows_to_add_list = []

    ROWS = original_galaxy

    # // horizontale uitbreiding
    for row_index, row in enumerate(ROWS):
        if added_new is True:
            added_new = False
            continue
        if all(character == '.' for character in row):
            new_row = ''
            for i in range(len(row)):
                new_row = new_row + '.'
            ROWS.insert(row_index, new_row)
            added_new = True

    max_x_cord = len(row)

    for i in range(0, max_x_cord):
        character_list = []
        for row in ROWS:
            character = row[i]
            character_list.append(character)

        if all(character == '.' for character in character_list):
            rows_to_add_list.append(i)

    new_rows_list = []
    for row in ROWS:
        number_to_add = 0
        row_list = list(row)
        for row_number in rows_to_add_list:
            new_number = row_number + number_to_add
            row_list.insert(new_number, '.')
            number_to_add += 1
            row = ''.join(row_list)
        new_rows_list.append(row)
    ROWS = new_rows_list
    return ROWS


galaxy_map = expand_galaxy(ROWS_og)

# // verzamel cords van galaxies
for map_number, map_row in enumerate(galaxy_map):
    x_axis = 0
    for character in map_row:
        if character == '#':
            galaxy_cords[galaxy_id] = (x_axis, map_number)
            galaxy_id += 1
        x_axis += 1


for key in galaxy_cords.keys():
    possible_paths = [item for item in galaxy_cords.keys()]
    possible_paths.remove(key)

    for possible_path in possible_paths:
        full_path = f'{min(key, possible_path)} to {max(key, possible_path)}'
        if full_path in path_distances.keys():
            pass
        else:
            start_location = galaxy_cords[key]
            end_location = galaxy_cords[possible_path]
            x_1 = max(start_location[0], end_location[0])
            x_2 = min(start_location[0], end_location[0])
            y_1 = max(start_location[1], end_location[1])
            y_2 = min(start_location[1], end_location[1])
            dif = (x_1 - x_2) + (y_1 - y_2)
            path_distances[full_path] = dif
            total_sum += dif

print(total_sum)





