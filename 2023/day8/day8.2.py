from math import lcm
INPUT = open('main.txt').read()

first_run = True

locations = {}
locations_with_a = []
locations_with_z = []
current_locations = []
new_locations = []
new_locations_second_loop = []
steps_per_location = []

first_location = 'AAA'
direction_index = 0
steps_taken = 0

# // verzamel directies
DIRECTIONS = INPUT.splitlines()[0]
directions_list = []


for direction in DIRECTIONS:
    directions_list.append(direction)


# // verzamel locaties
for location in INPUT.splitlines()[2:]:
    location_id, redirect_ids = location.split(' = ')
    locations[location_id] = redirect_ids
    if location_id[2] == 'A':
        locations_with_a.append(location_id)


for item in locations_with_a:
    current_location = item
    steps_taken = 0
    direction_index = 0
    while True:
        try:
            direction = directions_list[direction_index]
        except IndexError:
            direction_index = 0
            direction = directions_list[direction_index]
        # print(direction)

        if direction == 'L':
            current_location = locations[current_location][1:4]
        else:
            current_location = locations[current_location][6:9]

        if current_location[2] == 'Z':
            steps_taken += 1
            steps_per_location.append(steps_taken)
            break
        else:
            steps_taken += 1
            direction_index += 1

final_ans = lcm(*steps_per_location)

print(final_ans)