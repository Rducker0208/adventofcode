games = open('main.txt').read().splitlines()
power_sum = 0

for game in games:
    highest_red = 0
    highest_green = 0
    highest_blue = 0
    hands = game.split(';')
    for hand in hands:
        game_id = hand.split(':')
        try:
            hand = game_id[1]
        except IndexError:
            hand = game_id[0]
        cubes = hand.split(',')
        for item in cubes:
            if 'red' in item:
                red_cubes = item.split('red')[0]
                if int(red_cubes) > highest_red:
                    highest_red = int(red_cubes)
            if 'blue' in item:
                blue_cubes = item.split('blue')[0]
                if int(blue_cubes) > highest_blue:
                    highest_blue = int(blue_cubes)
            if 'green' in item:
                green_cubes = item.split('green')[0]
                if int(green_cubes) > highest_green:
                    highest_green = int(green_cubes)
    sum_to_add = highest_red * highest_green * highest_blue
    power_sum = power_sum + sum_to_add
print(power_sum)
