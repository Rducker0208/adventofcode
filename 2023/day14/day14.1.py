INPUT = open('main.txt').read()

round_stone_locations = []
cube_stone_locations = []

rows = {}

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


def find_new_location(original_x, original_y):
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


for y, row in rows.items():
    for x, character in enumerate(row):
        cords = (x, y)
        if cords in round_stone_locations:
            find_new_location(x, y)

total = 0
for location in round_stone_locations:
    total += location[1]

print(total)