import pprint

directions = open('sample.txt').read()

# // x, y
locations = [[1000, 1000] for i in range(10)]

# index 0 = new, index 10 = oldest
visited_locs = [[1000, 1000]]
move = 0


def check_distance(head_loc, tail_loc):
    manhattan_distance = abs((head_loc[0] - tail_loc[0])) + abs((head_loc[1] - tail_loc[1]))
    return manhattan_distance


def get_neighbouring_locations(head_loc, tail_loc):
    head_locations = [(head_loc[0] - 1, y) for y in [head_loc[1] - 1, head_loc[1], head_loc[1] + 1]]  # // links
    head_locations.extend([(head_loc[0] + 1, y) for y in [head_loc[1] - 1, head_loc[1], head_loc[1] + 1]])  # // rechts
    head_locations.append((head_loc[0], head_loc[1] + 1))  # // boven
    head_locations.append((head_loc[0], head_loc[1] - 1))  # // beneden

    tailing_locations = [(tail_loc[0] - 1, y) for y in [tail_loc[1] - 1, tail_loc[1], tail_loc[1] + 1]]  # // links
    tailing_locations.extend([(tail_loc[0] + 1, y) for y in [tail_loc[1] - 1, tail_loc[1], tail_loc[1] + 1]])  # // rechts
    tailing_locations.append((tail_loc[0], tail_loc[1] + 1))  # // boven
    tailing_locations.append((tail_loc[0], tail_loc[1] - 1))  # // beneden

    optimal_distance = 10 ** 100
    optimal_loc = None
    for location in head_locations:
        if location in tailing_locations:
            distance_to_head = check_distance(head_loc, location)
            if distance_to_head < optimal_distance:
                optimal_distance = distance_to_head
                optimal_loc = location

    return optimal_loc


def draw_grid(locations_visited, lowest_y, highest_y, lowest_x, highest_x):
    grid_dict = {}
    for y in range(lowest_y[1], highest_y[1] + 1):
        y_string = ''
        for x in range(lowest_x[0], highest_x[0] + 1):
            if [x, y] in locations_visited:
                y_string += '#'
            else:
                y_string += '.'

        if y < 1000:
            y = f' {y}'
        else:
            y = str(y)
        grid_dict[y] = y_string

    pprint.pprint(grid_dict)


for full_direction in directions.splitlines():
    direction, steps = full_direction.split()
    print(direction, steps)
    print(150 * '_')
    for i in range(int(steps)):
        for index in range(10):
            if index == 0:
                head_location = locations.pop(0)
                if direction == 'U':
                    head_location[1] -= 1
                elif direction == 'D':
                    head_location[1] += 1
                elif direction == 'L':
                    head_location[0] -= 1
                elif direction == 'R':
                    head_location[0] += 1
                locations.insert(0, head_location)

            else:
                leading_location = locations.pop(index - 1)
                tailing_location = locations.pop(index - 1)
                distance = check_distance(leading_location, tailing_location)

                if distance == 1:
                    pass

                elif distance == 2:
                    if leading_location[0] != tailing_location[0] and leading_location[1] != tailing_location[1]:
                        pass
                    else:
                        if direction == 'U':
                            tailing_location = [tailing_location[0], tailing_location[1] - 1]
                        elif direction == 'D':
                            tailing_location = [tailing_location[0], tailing_location[1] + 1]
                        elif direction == 'L':
                            tailing_location = [tailing_location[0] - 1, tailing_location[1]]
                        elif direction == 'R':
                            tailing_location = [tailing_location[0] + 1, tailing_location[1]]

                elif distance == 3 or distance > 3:
                    tailing_location = get_neighbouring_locations(leading_location, tailing_location)

                locations.insert(index - 1, leading_location)
                locations.insert(index, tailing_location)
                tailing_loc_list = [locations[9][0], locations[9][1]]

                if tailing_loc_list not in visited_locs:
                    visited_locs.append(tailing_loc_list)

        print(locations)
    print(150 * '_')


print(len(visited_locs))
print(visited_locs)

draw_grid(visited_locs, min(visited_locs, key=lambda x: x[1]), max(visited_locs, key=lambda x: x[1]), min(visited_locs, key=lambda x: x[0]), max(visited_locs, key=lambda x: x[0]))

