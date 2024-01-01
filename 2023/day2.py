import aoc_lube
import re
import pprint
games = aoc_lube.fetch(year=2023, day=2).splitlines()
max_red = 12
max_green = 13
max_blue = 14
possible_games_sum = 0

for game in games:
    print(game)
    game_possible = True
    game_id = None
    hands = game.split(';')
    for hand in hands:
        game_id = hand.split(':')
        try:
            hand = game_id[1]
        except IndexError:
            hand = game_id[0]
        cubes = hand.split(',')
        for item in cubes:
            # print(item)
            if 'red' in item:
                # print('-----red-------')
                red_cubes = item.split('red')[0]
                # print(red_cubes)
                if int(red_cubes) > max_red:
                    game_possible = False
            if 'blue' in item:
                # print('------blue-------')
                blue_cubes = item.split('blue')[0]
                # print(blue_cubes)
                if int(blue_cubes) > max_blue:
                    game_possible = False
            if 'green' in item:
                # print('-------green-------')
                green_cubes = item.split('green')[0]
                # print(green_cubes)
                if int(green_cubes) > max_green:
                    game_possible = False
    if game_possible is True:
        print(game)
        game_id = game.split(':')[0]
        print(game_id)
        game_nummer = game_id.split('Game')[1]
        print(game_nummer)
        possible_games_sum = possible_games_sum + int(game_nummer)
    else:
        print('impossible')
    print(possible_games_sum)

