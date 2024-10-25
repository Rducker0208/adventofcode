INPUT = open('main.txt').read()

games = INPUT.splitlines()
your_score = 0

# A & X = rock
# B & Y = paper
# C & Z = scisor

game_state_values = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

hand_values = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

hand_to_choose = {
    'A Z': 'Y',
    'A Y': 'X',
    'A X': 'Z',
    'B Z': 'Z',
    'B Y': 'Y',
    'B X': 'X',
    'C Z': 'X',
    'C Y': 'Z',
    'C X': 'Y',
}

for game in games:
    hand_chosen = hand_to_choose[game]
    your_score += (hand_values[hand_chosen] + game_state_values[game[-1]])

print(your_score)
