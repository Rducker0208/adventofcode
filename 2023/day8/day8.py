import aoc_lube

INPUT = aoc_lube.fetch(year=2023, day=8)

locations = {}
first_location = 'AAA'
start_direction_index = 0
start_steps = 0

# // verzamel directies
DIRECTIONS = INPUT.splitlines()[0]
directions_list = []


for direction in DIRECTIONS:
    directions_list.append(direction)


# // verzamel locaties
for location in INPUT.splitlines()[2:]:
    location_id, redirect_ids = location.split(' = ')
    locations[location_id] = redirect_ids


def goto_new_location(current_location, direction_index, total_steps):

    while True:
        # // verzamel directie
        try:
            direction_to_go = directions_list[direction_index]
        except IndexError:
            direction_index = 0
            direction_to_go = directions_list[direction_index]

        # // verzamel nieuew locatie
        if direction_to_go == 'L':
            current_location = locations[current_location][1:4]
            print(current_location)

        # // direction is rechts
        else:
            current_location = locations[current_location][6:9]

        if current_location == 'ZZZ':
            print('arrived at z')
            total_steps += 1
            print(total_steps)
            break
        else:
            total_steps += 1
            direction_index += 1


goto_new_location(first_location, start_direction_index, start_steps)
