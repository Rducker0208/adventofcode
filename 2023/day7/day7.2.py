import re

HANDS = open('main.txt').read().splitlines()


possible_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
five_of_a_kinds, four_of_a_kinds, full_houses, three_of_a_kinds, two_pairs, one_pairs, high_cards = ([] for j in range(7))
win_condition_list = [five_of_a_kinds, four_of_a_kinds, full_houses, three_of_a_kinds, two_pairs, one_pairs, high_cards]

card_to_letter = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'T': 'e',
    '9': 'f',
    '8': 'g',
    '7': 'h',
    '6': 'i',
    '5': 'j',
    '4': 'k',
    '3': 'l',
    '2': 'm',
    'J': 'z',
}

letter_to_card = {
    'a': 'A',
    'b': 'K',
    'c': 'Q',
    'e': 'T',
    'f': '9',
    'g': '8',
    'h': '7',
    'i': '6',
    'j': '5',
    'k': '4',
    'l': '3',
    'm': '2',
    'z': 'J'

}

card_to_number = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0,
}

number_to_card = {
    13: 'A',
    12: 'K',
    11: 'Q',
    9: 'T',
    8: '9',
    7: '8',
    6: '7',
    5: '6',
    4: '5',
    3: '4',
    2: '3',
    1: '2',
    0: 'J',
}

card_in_numbers_dict = {}

hand_data = {}


def find_best_option(hand_to_check):
    max_times = 0
    best_option = None
    for possible_card in possible_cards:
        amount_of_times = 0
        for car_found in re.finditer(possible_card, hand_to_check):
            amount_of_times += 1

        if max_times == 0:
            if possible_card != 'J':
                max_times = amount_of_times
                best_option = possible_card

        elif amount_of_times > max_times:
            if possible_card == 'J':
                pass
            else:
                best_option = possible_card
                max_times = amount_of_times

        elif amount_of_times == max_times:
            old_leter_value = card_to_number[best_option]
            new_letter_value = card_to_number[possible_card]

            if new_letter_value > old_leter_value:
                best_option = possible_card

    if max_times == 1:
        max_card_value = 0
        card_value_found = 0
        for possible_card in possible_cards:
            if possible_card in hand:
                card_value = card_to_number[possible_card]
                if card_value > max_card_value:
                    max_card_value = card_value

        best_option = number_to_card[max_card_value]
    return best_option


# // verkrijg kaart data en stop deze in een dictionary
for value in HANDS:
    cards, hand_value = value.split()
    hand_data[cards] = hand_value


# // ga elke mogelijke hand na
for hand in hand_data.keys():
    matching_cards = []
    card_numbers = {}

    hand_without_j = hand
    if hand_without_j == 'JJJJJ':
        hand_without_j = 'AAAAA'
    else:
        for card in hand_without_j:
            if card == 'J':
                new_letter = find_best_option(hand_without_j)
                hand_without_j = hand_without_j.replace(card, new_letter)

    # // ga elke kaart na om te kijken of deze in de hand zit
    for card in possible_cards:

        # // ga elke kaart na met regex
        for matching_card in re.finditer(card, hand_without_j):
            matching_cards.append(matching_card.group())

    # // check hoevaak in kaart in de hand zit en sla dit op in de dictionary
    for matching_card in matching_cards:
        card_numbers[matching_card] = matching_cards.count(matching_card)

    one_match = 0
    two_matches = 0
    three_matches = 0
    four_matches = 0
    five_matches = 0

    # //  zet dit om naar variables
    for card_count in card_numbers.values():
        if card_count == 1:
            one_match += 1
        elif card_count == 2:
            two_matches += 1
        elif card_count == 3:
            three_matches += 1
        elif card_count == 4:
            four_matches += 1
        elif card_count == 5:
            five_matches += 1

    # // check wincondities
    if five_matches == 1:
        five_of_a_kinds.append(hand)
    elif four_matches == 1 and one_match == 1:
        four_of_a_kinds.append(hand)
    elif three_matches == 1 and two_matches == 1:
        full_houses.append(hand)
    elif three_matches == 1 and one_match == 2:
        three_of_a_kinds.append(hand)
    elif two_matches == 2 and one_match == 1:
        two_pairs.append(hand)
    elif two_matches == 1 and one_match == 3:
        one_pairs.append(hand)
    elif one_match == 5:
        high_cards.append(hand)


def sort_list(list_to_sort):
    new_list = []
    new_list_back_to_card = []
    for card_set in list_to_sort:
        for card in card_set:  # noqa
            new_card = card_to_letter[card]
            card_set = card_set.replace(card, new_card)
        new_list.append(card_set)
    list_sorted_by_letter = sorted(new_list)

    for letter_set in list_sorted_by_letter:
        for letter in letter_set:
            new_letter = letter_to_card[letter]
            letter_set = letter_set.replace(letter, new_letter)
        new_list_back_to_card.append(letter_set)

    return new_list_back_to_card


final_list = []

# // ga elke lijst met wincondities door van waardevol naar niet waardevol
for list_with_set in win_condition_list:
    if list_with_set:
        sorted_list = sort_list(list_with_set)
        for item in sorted_list:
            final_list.append(item)

final_list.reverse()

total_sum = 0
for index, hand in enumerate(final_list):
    rank = index + 1
    value = hand_data[hand]
    sum_to_add = rank * int(value)
    total_sum += sum_to_add

print(total_sum)