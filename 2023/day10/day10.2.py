INPUT = open('main.txt').read()

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

# // vind startpunt oftewel de index van S
for row_number, row in row_dict.items():
    if 'S' in row:
        S_index = (row.index('S'), row_number)
        loop_cords_list.append(S_index)
        break


# // zoek naar paden die langs de S liggen om te kijken welke kant je op kunt
def get_loop_start():
    S_x = S_index[0]
    S_y = S_index[1]

    # // pad begint rechts
    if row_dict[S_y][S_x + 1] in ['-', 'J', '7']:
        starting_point = (S_x + 1, S_y)
        loop_cords_list.append(starting_point)
        direction = 'right'
        return starting_point, direction

    # // pad begint links
    elif row_dict[S_y][S_x - 1] in ['L', '-', 'F']:
        starting_point = (S_x - 1, S_y)
        loop_cords_list.append(starting_point)
        direction = 'left'
        return starting_point, direction

    # // het pad begint boven
    elif row_dict[S_y - 1][S_x] in ['7', 'F', '|']:
        starting_point = (S_x, S_y - 1)
        loop_cords_list.append(starting_point)
        direction = 'up'
        return starting_point, direction

    # het pad begint benden
    elif row_dict[S_y + 1][S_x] in ['|', 'J', 'L']:
        starting_point = (S_x, S_y + 1)
        loop_cords_list.append(starting_point)
        direction = 'down'
        return starting_point, direction


current_location, current_direction = get_loop_start()


# // kijk welke kant je op moet om loop te volgen
def get_direction(original_direction, location_to_check):

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
    loop_cords_list.append(current_location)

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
        if location_to_check in loop_cords_list:
            character = row_dict[y_cord][x_cord]
            if character == '|':
                interceptions += 1
            else:
                if loop is False:
                    streak_start_char = character
                    loop = True
                else:
                    if character == '-':
                        pass
                    else:
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
                interceptions += 1
                loop_valid = None
                loop = False

            elif loop_valid is False:
                loop_valid = None
                loop = False
        x_cord -= 1

    if interceptions % 2 != 0 and interceptions != 0:
        new_results.append(location)

print(len(new_results))