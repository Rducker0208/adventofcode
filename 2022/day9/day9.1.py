directions = open('main.txt').read()

# // x, y
tail_pos = [1000, 1000]
head_pos = [1000, 1000]
visited_locs = [[1000, 1000]]
move = 0


def check_distance(head_loc, tail_loc):
    manhattan_distance = abs((head_loc[0] - tail_loc[0])) + abs((head_loc[1] - tail_loc[1]))
    return manhattan_distance


for full_direction in directions.splitlines():
    direction, steps = full_direction.split()
    for i in range(int(steps)):
        if direction == 'U':
            head_pos[1] -= 1
        elif direction == 'D':
            head_pos[1] += 1
        elif direction == 'L':
            head_pos[0] -= 1
        elif direction == 'R':
            head_pos[0] += 1

        # print('_' * 125)
        # print(head_pos, tail_pos)
        distance = abs((head_pos[0] - tail_pos[0])) + abs((head_pos[1] - tail_pos[1]))
        # print(distance)

        if distance == 2:
            if head_pos[0] != tail_pos[0] and head_pos[1] != tail_pos[1]:
                pass
            else:
                if direction == 'U':
                    tail_pos = [tail_pos[0], tail_pos[1] - 1]
                elif direction == 'D':
                    tail_pos = [tail_pos[0], tail_pos[1] + 1]
                elif direction == 'L':
                    tail_pos = [tail_pos[0] - 1, tail_pos[1]]
                elif direction == 'R':
                    tail_pos = [tail_pos[0] + 1, tail_pos[1]]

        elif distance == 3:
            if direction == 'U':
                tail_pos = [head_pos[0], head_pos[1] + 1]
            elif direction == 'D':
                tail_pos = [head_pos[0], head_pos[1] - 1]
            elif direction == 'L':
                tail_pos = [head_pos[0] + 1, head_pos[1]]
            elif direction == 'R':
                tail_pos = [head_pos[0] - 1, head_pos[1]]

        if tail_pos not in visited_locs:
            visited_locs.append(tail_pos)

print(len(visited_locs))




