games = open('main.txt').read().splitlines()
max_red = 12
max_green = 13
max_blue = 14
possible_games_sum = 0

for game in games:
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
            if 'red' in item:
                red_cubes = item.split('red')[0]
                if int(red_cubes) > max_red:
                    game_possible = False
            if 'blue' in item:
                blue_cubes = item.split('blue')[0]
                if int(blue_cubes) > max_blue:
                    game_possible = False
            if 'green' in item:
                green_cubes = item.split('green')[0]
                if int(green_cubes) > max_green:
                    game_possible = False
    if game_possible is True:
        game_id = game.split(':')[0]
        game_nummer = game_id.split('Game')[1]
        possible_games_sum = possible_games_sum + int(game_nummer)
print(possible_games_sum)

