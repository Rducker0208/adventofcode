import copy

directions = open('main.txt').read()
current_position = [0, 0]
visited_houses = [[0, 0]]
house_count = 1

for direction in directions:
    if direction == '^':
        current_position[1] += 1
    elif direction == 'v':
        current_position[1] -= 1
    elif direction == '>':
        current_position[0] += 1
    else:
        current_position[0] -= 1

    if current_position not in visited_houses:
        visited_houses.append(copy.copy(current_position))
        house_count += 1

print(house_count)