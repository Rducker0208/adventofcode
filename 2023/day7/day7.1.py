import re

HANDS = open('main.txt').read().splitlines()

possible_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
five_of_a_kinds, four_of_a_kinds, full_houses, three_of_a_kinds, two_pairs, one_pairs, high_cards = ([] for j in range(7))
win_condition_list = [five_of_a_kinds, four_of_a_kinds, full_houses, three_of_a_kinds, two_pairs, one_pairs, high_cards]
hand_data = {}
card_to_letter = {
    'A': 'a',
    'K': 'b',
    'Q': 'c',
    'J': 'd',
    'T': 'e',
    '9': 'f',
    '8': 'g',
    '7': 'h',
    '6': 'i',
    '5': 'j',
    '4': 'k',
    '3': 'l',
    '2': 'm',
}

letter_to_card = {
    'a': 'A',
    'b': 'K',
    'c': 'Q',
    'd': 'J',
    'e': 'T',
    'f': '9',
    'g': '8',
    'h': '7',
    'i': '6',
    'j': '5',
    'k': '4',
    'l': '3',
    'm': '2',

}

card_in_numbers_dict = {}

# // verkrijg kaart data en stop deze in een dictionary
for value in HANDS:
    cards, hand_value = value.split()
    hand_data[cards] = hand_value

# // ga elke mogelijke hand na
for hand in hand_data.keys():
    matching_cards = []
    card_numbers = {}

    # // ga elke kaart na om te kijken of deze in de hand zit
    for card in possible_cards:

        # // ga elke kaart na met regex
        for matching_card in re.finditer(card, hand):
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