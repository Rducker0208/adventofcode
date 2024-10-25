import copy

x_rows = {num: line for num, line in enumerate(open('main.txt').read().splitlines())}
rocks = []
seen = []
seen_locations = []
count = 0
step_dict = {num: [] for num in range(65)}
queue = None

for num, row in x_rows.items():
    if 'S' in row:
        start_point = (num, row.index('S'))
        queue = [start_point]
        step_dict[0].append(start_point)

for y_val, row in x_rows.items():
    for x_val, char in enumerate(row):
        if char == '#':
            rocks.append((x_val, y_val))


def find_neighbours(location):
    locations_to_send = []
    x_cord, y_cord = location
    if x_cord > 0:
        locations_to_send.append((location[0] - 1, location[1]))
    if x_cord < len(x_rows):
        locations_to_send.append((location[0] + 1, location[1]))
    if y_cord > 0:
        locations_to_send.append((location[0], location[1] - 1))
    if y_cord < len(x_rows[0]):
        locations_to_send.append((location[0], location[1] + 1))
    return locations_to_send


for i in range(64):
    new_queue = []
    while len(queue) > 0:
        loc = queue.pop(0)
        if loc not in seen_locations:
            seen_locations.append(loc)
            neighbours = find_neighbours(loc)
            for item in neighbours:
                if item not in new_queue and item not in seen_locations and x_rows[item[1]][item[0]] != '#':
                    new_queue.append(item)
                    step_dict[i + 1].append(item)

    queue = copy.deepcopy(new_queue)

for num, loc_list in step_dict.items():
    if num % 2 != 0:
        pass
    else:
        count += len(loc_list)

print(count)