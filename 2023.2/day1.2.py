import aoc_lube
import re
LINES = aoc_lube.fetch(year=2023, day=1).splitlines()
# LINES = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
lines = 0
index = 0
total_number = 0
ValueError_count = 0
nummers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
spelled_nummers = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
reverse_spelled_nummers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

print(LINES)

for string in LINES:
    index_list = []
    index_library = {}
    print(string)
    for number in spelled_nummers.keys():
        if number in string:
            indexes = [m.start() for m in re.finditer(number, string)]
            for item in indexes:
                index_library[item] = spelled_nummers.get(number)

    for number in reverse_spelled_nummers.keys():
        if str(number) in string:
            print(str(number))
            indexes = [m.start() for m in re.finditer(str(number), string)]
            for item in indexes:
                index_library[item] = number

    print(index_library)
    index_list = []
    for index in index_library.keys():
        index_list.append(index)
    index_list.sort()
    print(index_list)
    first_number = index_library.get(index_list[0])
    last_number = index_library.get(index_list[-1])
    number_to_add = int(f'{first_number}{last_number}')
    total_number = total_number + number_to_add
    print(number_to_add)
print(total_number)
