import aoc_lube

LINES = open('main.txt').read().splitlines()
lines = 0
total_number = 0
nummers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print(LINES)

for item in LINES:
    string_counter = 0
    numbers = 0
    first_number_found = False
    first_number = ''
    for letter_count in range(len(item)):
        letter = item[letter_count]
        if letter in nummers:
            if first_number_found is False:
                first_number = letter
                last_number = letter
                numbers = f'{first_number}{last_number}'
                first_number_found = True
            else:
                last_number = letter
                numbers = f'{first_number}{last_number}'
    print(numbers)
    total_number = total_number + int(numbers)
print(total_number)