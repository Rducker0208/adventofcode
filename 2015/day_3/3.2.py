import copy

directions = open('main.txt').read()
visited_houses = [[0, 0]]
house_count = 1
santa_pos = [0, 0]
robo_pos = [0, 0]

turn = 'santa'

for direction in directions:
    if turn == 'santa':
        turn = 'robot'

        if direction == '^':
            santa_pos[1] += 1
        elif direction == 'v':
            santa_pos[1] -= 1
        elif direction == '>':
            santa_pos[0] += 1
        else:
            santa_pos[0] -= 1

        if santa_pos not in visited_houses:
            visited_houses.append(copy.copy(santa_pos))
            house_count += 1

    else:
        turn = 'santa'

        if direction == '^':
            robo_pos[1] += 1
        elif direction == 'v':
            robo_pos[1] -= 1
        elif direction == '>':
            robo_pos[0] += 1
        else:
            robo_pos[0] -= 1

        if robo_pos not in visited_houses:
            visited_houses.append(copy.copy(robo_pos))
            house_count += 1

print(house_count)