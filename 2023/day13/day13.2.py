INPUT = open('main.txt').read()

RAW_INPUT_lIST = INPUT.split('\n\n')

row = None
patern_list = []
matches_list = []
total = 0


# verzamel alle patronen
for item in RAW_INPUT_lIST:
    characters_list = []
    list_of_lines = item.split('\n')
    character = ''
    for line in list_of_lines:
        character = character + '\n' + line
    patern_list.append(character)


# ga elk patroon na
for item in patern_list:
    match = None
    vertical_rows = {}
    horizontal_rows = {}
    horizontal_row_count = 0

    # verzamel horizontale rijen (y-assen)
    for row_id, row in enumerate(item[1:].splitlines()):
        horizontal_rows[row_id + 1] = row
        horizontal_row_count += 1

    # verzamel verticale rijen(x-assen)
    for x_axis in range(len(row)):
        x_values = []
        for row in item[1:].splitlines():
            x_character = row[x_axis]
            x_values.append(x_character)
        vertical_rows[x_axis + 1] = x_values

    # // begin met zoeken op verschillen in x_as
    last_line_number = 1
    next_line_number = 2

    while True:
        if last_line_number == len(horizontal_rows) or match is not None:
            break
        differences = 0
        last_line = horizontal_rows[last_line_number]
        next_line = horizontal_rows[next_line_number]

        for last_line_character, next_line_character in zip(last_line, next_line):
            if last_line_character != next_line_character:
                differences += 1

        current_cords = (last_line_number, next_line_number)

        if differences == 0 or differences == 1:
            left_cords = last_line_number
            right_cords = next_line_number
            while True:
                try:

                    left_cords -= 1
                    right_cords += 1
                    last_line = horizontal_rows[left_cords]
                    next_line = horizontal_rows[right_cords]
                    for last_line_character, next_line_character in zip(last_line, next_line):
                        if last_line_character != next_line_character:
                            differences += 1

                except KeyError:
                    if differences == 1:
                        match = ('horizontal', current_cords)
                        matches_list.append(match)
                        break
                    else:
                        break

        last_line_number += 1
        next_line_number += 1

    if match is None:
        current_row_number = 1
        next_row_number = 2

        while True:
            if current_row_number == len(vertical_rows):
                break

            current_x_cords = vertical_rows[current_row_number]
            next_x_cords = vertical_rows[next_row_number]

            vertical_differences = 0

            for current_x, next_x in zip(current_x_cords, next_x_cords):
                if current_x != next_x:
                    vertical_differences += 1

            currend_cords = (current_row_number, next_row_number)
            if vertical_differences == 0 or vertical_differences == 1:
                left_cords = current_row_number
                right_cords = next_row_number

                while True:
                    try:
                        left_cords -= 1
                        right_cords += 1

                        left_line = vertical_rows[left_cords]
                        right_line = vertical_rows[right_cords]

                        for left_line_chraracter, right_line_character in zip(left_line, right_line):
                            if left_line_chraracter != right_line_character:
                                vertical_differences += 1

                    except KeyError:
                        if vertical_differences == 1:
                            match = ('vertical', currend_cords)
                            matches_list.append(match)
                            break
                        else:
                            break

            current_row_number += 1
            next_row_number += 1


for dimension, sides in matches_list:
    lower_side = sides[0]
    higher_side = sides[1]
    if dimension == 'horizontal':
        total += lower_side * 100
    elif dimension == 'vertical':
        total += lower_side

print(total)