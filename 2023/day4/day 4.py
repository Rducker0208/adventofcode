import aoc_lube
LINES = aoc_lube.fetch(year=2023, day=4).splitlines()

# LINES = """card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

total_sum = 0
for card in LINES:

    winning_numbers_list = []
    numbers_you_have_list = []
    matching_cards_list = []

    card_id = card.split(':')[0]
    card_numbers = card.split(':')[1]
    winning_numbers = card_numbers.split('|')[0]
    numbers_you_have = card_numbers.split('|')[1]

    # verzamel winnende nummers
    for winning_number in winning_numbers.split():
        winning_numbers_list.append(winning_number)

    # verzamel kaart nummers
    for number_you_have in numbers_you_have.split():
        numbers_you_have_list.append(number_you_have)

    # zoek matchende nummers
    for number_you_have in numbers_you_have_list:
        if number_you_have in winning_numbers_list:
            print(f'Match!!!! {number_you_have}')
            matching_cards_list.append(number_you_have)

    print(matching_cards_list)

    # puntentelling
    if len(matching_cards_list) == 0:
        card_points = 0
    elif len(matching_cards_list) == 1:
        card_points = 1
    else:
        card_points = 1
        matching_cards_list.pop(-1)
        for item in matching_cards_list:
            card_points = card_points * 2

    print(f'{card_id}: {card_points} points')
    total_sum = total_sum + card_points
print(f'TOTAL: {total_sum}')




