LINES = open('main.txt').read().splitlines()
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
            matching_cards_list.append(number_you_have)

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

    total_sum = total_sum + card_points
print(f'TOTAL: {total_sum}')




