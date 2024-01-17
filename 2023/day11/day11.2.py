ROWS = open('main.txt').read().splitlines()
extra_x = 0
extra_y = 0


galaxy_cords = {}
path_distances = {}
x_to_characters_dict = {}
rows_to_add_list = []
galaxy_id = 1
x_axis = 0
total_sum = 0

row = None

for x_axis_to_check in range(len(ROWS)):
    character_list = []
    for item in ROWS:
        character = item[x_axis_to_check]
        character_list.append(character)
    x_to_characters_dict[x_axis_to_check] = character_list


def find_extra_y(original_y):
    y = 0
    y_to_add = 0
    while not y > original_y:
        if all(symbol == '.' for symbol in ROWS[y]):
            y_to_add += 999999
        y += 1
    return y_to_add


def find_extra_x(original_x):
    x = 0
    x_to_add = 0

    while not x > original_x:
        if all(characters == '.' for characters in x_to_characters_dict[x]):
            x_to_add += 999999
        x += 1
    return x_to_add


# // verzamel cords van galaxies
for map_number, map_row in enumerate(ROWS):
    x_axis = 0
    for character in map_row:
        if character == '#':
            galaxy_cords[galaxy_id] = (x_axis + find_extra_x(x_axis), map_number + find_extra_y(map_number))
            galaxy_id += 999999
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
