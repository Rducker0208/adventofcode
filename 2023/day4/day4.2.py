import aoc_lube

LINES = aoc_lube.fetch(year=2023, day=4).splitlines()

card_dict = {}

total_sum = 0
card_index = 1

for card in LINES:
    card_dict[card_index] = card
    card_index += 1

for card in LINES:
    winning_numbers_list = []
    numbers_you_have_list = []
    matching_numbers_list = []

    card_id = card.split(':')[0]
    card_id_number = int(card_id.split('Card')[1])
    card_numbers = card.split(':')[1]
    winning_numbers = card_numbers.split('|')[0]
    numbers_you_have = card_numbers.split('|')[1]

    # verzamel winnende nummers
    for winning_number in winning_numbers.split():
        winning_numbers_list.append(winning_number)

    # verzamel kaart nummers
    for number_you_have in numbers_you_have.split():
        numbers_you_have_list.append(number_you_have)

    for number_you_have in numbers_you_have_list:
        if number_you_have in winning_numbers_list:
            matching_numbers_list.append(number_you_have)

    for matching_number in matching_numbers_list:
        card_id_number += 1
        LINES.append(card_dict.get(int(card_id_number)))

print(f'FINAL_RESULT: {len(LINES)}')


