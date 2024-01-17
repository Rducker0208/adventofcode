INPUT = open('main.txt').read()

row_dict = {}
steps_taken_dict = {}
current_location_dict = {}  # y-axis, x-axis
original_direction_dict = {}
S_index = None
new_location = None
path = None

# // verzamel row data
for row_number, row in enumerate(INPUT.splitlines()):
    row_dict[row_number + 1] = row

# // vind startpunt
for row_number, row in row_dict.items():
    if 'S' in row:
        S_index = (row_number, row.index('S'))
        break


def find_neighbours():

    # // boven
    if row_dict[S_index[0] - 1][S_index[1]] in ['|', '7', 'F']:
        neighbouring_cords = (S_index[0] - 1, S_index[1])
        steps_taken_dict[neighbouring_cords] = 0
        current_location_dict[neighbouring_cords] = neighbouring_cords
        original_direction_dict[neighbouring_cords] = 'up'

    # // beneden
    if row_dict[S_index[0] + 1][S_index[1]] in ['|', 'L', 'J']:
        neighbouring_cords = (S_index[0] + 1, S_index[1])
        steps_taken_dict[neighbouring_cords] = 0
        current_location_dict[neighbouring_cords] = neighbouring_cords
        original_direction_dict[neighbouring_cords] = 'down'

    # // links
    if row_dict[S_index[0]][S_index[1] - 1] in ['-', 'L', 'F']:
        neighbouring_cords = (S_index[0], S_index[1] - 1)
        steps_taken_dict[neighbouring_cords] = 0
        current_location_dict[neighbouring_cords] = neighbouring_cords
        original_direction_dict[neighbouring_cords] = 'left'

    # // rechts
    if row_dict[S_index[0]][S_index[1] + 1] in ['7', 'J', '-']:
        neighbouring_cords = (S_index[0], S_index[1] + 1)
        steps_taken_dict[neighbouring_cords] = 0
        current_location_dict[neighbouring_cords] = neighbouring_cords
        original_direction_dict[neighbouring_cords] = 'right'


find_neighbours()


def get_direction(original_path, location_to_check):
    # row_dict[location_to_check[0]][location_to_check[1]] = huidige locatie

    new_direction = None

    if row_dict[location_to_check[0]][location_to_check[1]] == '|':
        if original_direction_dict[original_path] == 'down':
            new_direction = 'down'
        else:
            new_direction = 'up'

    elif row_dict[location_to_check[0]][location_to_check[1]] == 'L':
        if original_direction_dict[original_path] == 'down':
            new_direction = 'right'
        else:
            new_direction = 'up'

    elif row_dict[location_to_check[0]][location_to_check[1]] == '-':
        if original_direction_dict[original_path] == 'right':
            new_direction = 'right'
        else:
            new_direction = 'left'

    elif row_dict[location_to_check[0]][location_to_check[1]] == 'J':
        if original_direction_dict[original_path] == 'right':
            new_direction = 'up'
        else:
            new_direction = 'left'

    elif row_dict[location_to_check[0]][location_to_check[1]] == '7':
        if original_direction_dict[original_path] == 'up':
            new_direction = 'left'
        else:
            new_direction = 'down'

    elif row_dict[location_to_check[0]][location_to_check[1]] == 'F':
        if original_direction_dict[original_path] == 'up':
            new_direction = 'right'
        else:
            new_direction = 'down'

    return new_direction


# // main loop die kijkt of destinaties hetzelfe zijn
while True:
    for path, current_location in current_location_dict.items():
        direction = get_direction(path, current_location)

        if direction == 'up':
            new_location = (current_location[0] - 1, current_location[1])

        elif direction == 'down':
            new_location = (current_location[0] + 1, current_location[1])

        elif direction == 'left':
            new_location = (current_location[0], current_location[1] - 1)

        elif direction == 'right':
            new_location = (current_location[0], current_location[1] + 1)

        current_location_dict[path] = new_location
        original_direction_dict[path] = direction
        steps_taken_dict[path] += 1
        current_test_location = new_location

    if all(current_locations == new_location for current_locations in current_location_dict.values()):
        print(steps_taken_dict[path] + 1)
        quit()
