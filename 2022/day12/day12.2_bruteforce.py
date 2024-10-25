import time

horizontal_rows = open('main.txt').read().splitlines()
vertical_rows = [[row[x] for row in horizontal_rows] for x in range(len(horizontal_rows[-1]))]
start_locations = [(row_id, row.index('S'), 0) for row_id, row in enumerate(vertical_rows) if 'S' in row]
start_locations.extend([(x, y, 0) for y, row in enumerate(horizontal_rows) for x, char in enumerate(row) if char == 'a'])
end_point = [(row_id, row.index('E')) for row_id, row in enumerate(vertical_rows) if 'E' in row][0]

new_queue = []
steps_taken_to_reach = []

start = time.time()


def find_neighbours(x, y, steps):
    neighbour_list = []
    if x > 0:
        neighbour_list.append((x - 1, y, steps + 1))
    if x < len(horizontal_rows[0]) - 1:
        neighbour_list.append((x + 1, y, steps + 1))

    if y > 0:
        neighbour_list.append((x, y - 1, steps + 1))
    if y < len(horizontal_rows) - 1:
        neighbour_list.append((x, y + 1, steps + 1))

    return neighbour_list


for starting_point in start_locations:
    queue = [starting_point]
    visited_locations = []
    while len(queue) > 0:
        location = queue.pop(0)
        x_cord, y_cord, steps_amount = location
        location_height = ord(horizontal_rows[y_cord][x_cord]) - 96
        if location_height == -27:
            steps_taken_to_reach.append(steps_amount)
            break

        elif location_height == - 13:
            location_height = 1

        if (x_cord, y_cord) not in visited_locations:
            visited_locations.append((x_cord, y_cord))
            neighbours = find_neighbours(x_cord, y_cord, steps_amount)

            for neighbour in neighbours:
                x, y, steps = neighbour

                if (x, y) not in visited_locations:
                    new_height = ord(horizontal_rows[y][x]) - 96
                    if new_height == -27:
                        new_height = 26

                    if new_height - 1 <= location_height:
                        queue.append(neighbour)

print(time.time() - start)
print(min(steps_taken_to_reach))