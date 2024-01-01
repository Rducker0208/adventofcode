import aoc_lube
import re

lines = aoc_lube.fetch(year=2023, day=3)

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

line_list = []
gear_dict = {}
neighbouring_numbers = None

line_counter = 0
for line in lines.split():
    line_list.append(f'{line}')
    line_counter += 1

print(line_list)
line_number = 0
total_sum = 0

# verzamel coordinaten voor gears
for line in line_list:
    for n in re.finditer(r"\*", line):
        if line_number in gear_dict.keys():
            index_list = []
            existing_indexes = gear_dict.get(line_number)
            for item in existing_indexes:
                index_list.append(item)
            index_list.append(n.start())
            gear_dict[line_number] = index_list
        else:
            index_list = []  # noqa
            index_list.append(n.start())
            gear_dict[line_number] = index_list

    line_number += 1
print(gear_dict)

for item in gear_dict.keys():
    gear_line = item
    gear_indexes = gear_dict.get(item)
    for gear in gear_indexes:
        neighbouring_numbers = []
        print(f'{gear_line}, {gear}')

        try:
            above_line = line_list[item - 1]
        except IndexError:
            above_line = None

        try:
            down_line = line_list[item + 1]
        except IndexError:
            down_line = None

        line_with_gear = line_list[item]

        print(above_line)
        print(line_with_gear)
        print(down_line)

        # check voor nummer links
        print(line_with_gear[gear - 1])
        if line_with_gear[gear - 1] in numbers:
            for m in re.finditer(r"(\d+)", line_with_gear):
                if m.end() == gear:
                    if m.group() not in neighbouring_numbers:
                        neighbouring_numbers.append(m.group())
                    print(f'Match links!!!!! {m.group()}')

        # check voor nummer rechts
        if line_with_gear[gear + 1] in numbers:
            for m in re.finditer(r"(\d+)", line_with_gear):
                if m.start() - 1 == gear:
                    if m.group() not in neighbouring_numbers:
                        neighbouring_numbers.append(m.group())
                    print(f'Match rechts!!!!! {m.group()}')

        # check for nummer boven
        if down_line is None:
            pass
        else:
            for index in range(gear - 1, gear + 2):
                if above_line[index] in numbers:
                    for m in re.finditer(r"(\d+)", above_line):
                        if gear in range(m.start() - 1, m.end() + 1):
                            if m.group() not in neighbouring_numbers:
                                neighbouring_numbers.append(m.group())
                            print(f'Match boven!!!!!!: {m.group()}')

        # check for nummer beneden
        if down_line is None:
            pass
        else:
            for index in range(gear - 1, gear + 2):
                if down_line[index] in numbers:
                    for m in re.finditer(r"(\d+)", down_line):
                        if gear in range(m.start() - 1, m.end() + 1):
                            if m.group() not in neighbouring_numbers:
                                neighbouring_numbers.append(m.group())
                            print(f'Match beneden!!!!!!: {m.group()}')

        print('#################################')
        if len(neighbouring_numbers) == 2:
            print(neighbouring_numbers)
            sum_to_add = int(neighbouring_numbers[0]) * int(neighbouring_numbers[1])
            total_sum = total_sum + sum_to_add
        else:
            print('There is not a valid gear')
            print(neighbouring_numbers)
        print('#################################')
print(total_sum)

