INPUT = open('main.txt').read()
RAW_INPUT_lIST = INPUT.split('\n\n')

patern_list = []
matches_list = []
total = 0


for item in RAW_INPUT_lIST:
    characters_list = []
    list_of_lines = item.split('\n')
    character = ''
    for line in list_of_lines:
        character = character + '\n' + line
    patern_list.append(character)


def check_horizontal_match(cords_up, cords_down):
    while True:
        try:
            cords_up -= 1
            cords_down += 1
            up_row = horizontal_rows[cords_up]
            down_row = horizontal_rows[cords_down]
            if up_row == down_row:
                pass
            else:
                return False
        except KeyError:
            return True


def check_vertical_match(cords_left, cords_right):
    while True:
        try:
            cords_left -= 1
            cords_right += 1
            if vertical_rows[cords_left] == vertical_rows[cords_right]:
                pass
            else:
                return False
        except KeyError:
            return True


for item in patern_list:
    match = None
    vertical_rows = {}
    horizontal_rows = {}
    horizontal_row_count = 0

    # verzamel horizontale rijen
    for row_number, row in enumerate(item[1:].splitlines()):
        horizontal_rows[row_number + 1] = row
        horizontal_row_count += 1

    row_length = len(row)

    for x_axis in range(row_length):
        x_values = []
        for row in item[1:].splitlines():
            x_character = row[x_axis]
            x_values.append(x_character)
        vertical_rows[x_axis + 1] = x_values

    start_row_up = 1
    start_row_down = 2
    left = 1
    right = 2

    while True:
        try:
            row_up = horizontal_rows[start_row_up]
            row_down = horizontal_rows[start_row_down]
            if row_up == row_down:
                if check_horizontal_match(start_row_up, start_row_down) is True:
                    match = ('horizontal', start_row_up, start_row_down)
                    matches_list.append(match)
                    break
            start_row_up += 1
            start_row_down += 1
        except KeyError:
            match = None
            break

    if match is None:
        while True:
            try:
                if vertical_rows[left] == vertical_rows[right]:
                    if check_vertical_match(left, right) is True:
                        match = ('vertical', left, right)
                        matches_list.append(match)
                        break
                left += 1
                right += 1

            except KeyError:
                match = None
                break


for dimension, lower_side, higher_side in matches_list:
    if dimension == 'horizontal':
        total += lower_side * 100
    elif dimension == 'vertical':
        total += lower_side

print(total)
