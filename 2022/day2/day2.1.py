INPUT = open('main.txt').read()

games = INPUT.splitlines()
your_score = 0

# A & X = rock
# B & Z = paper
# C & Y = scisor

hand_values = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

possible_games = {
    'A Y': 6,
    'A X': 3,
    'A Z': 0,
    'B Z': 6,
    'B Y': 3,
    'B X': 0,
    'C X': 6,
    'C Z': 3,
    'C Y': 0,
}

for game in games:
    your_score += (hand_values[game[-1]] + possible_games[game])

print(your_score)
