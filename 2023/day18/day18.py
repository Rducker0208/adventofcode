from pprint import pprint
import aoc_lube

INPUT = aoc_lube.fetch(year=2023, day=18)

grid_dict = {}
directions = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
boundary_locations = 0
seen_locations = [(0, 0)]
valid_lava_locations = []
position = (0, 0)

rules = INPUT.splitlines()


def shoelace():
    i = 1
    area = 0
    while i != len(seen_locations) - 1:
        x = seen_locations[i][0]
        previous_y = seen_locations[i - 1][1]
        next_y = seen_locations[i + 1][1]
        area += x * (next_y - previous_y)
        i += 1

    area //= 2
    return area


def picks(old_area, boundary_points):
    new_area = old_area - boundary_points // 2 + 1
    return new_area


for rule in rules:
    direction, step_amount, hex_value = rule.split()
    step_amount = int(step_amount)
    boundary_locations += step_amount

    if direction == 'R':
        seen_locations.append((position[0] + step_amount, position[1]))

    elif direction == 'L':
        seen_locations.append((position[0] - step_amount, position[1]))

    elif direction == 'U':
        seen_locations.append((position[0], position[1] - step_amount))

    else:
        seen_locations.append((position[0], position[1] + step_amount))

    position = seen_locations[-1]

area = shoelace()
final_area = picks(area, boundary_locations)
final_ans = final_area + boundary_locations
print(final_ans)