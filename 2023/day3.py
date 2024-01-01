import aoc_lube
import re
lines = aoc_lube.fetch(year=2023, day=3)
# lines = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..
# """

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '&', '*', '=', '_', '+', '/', '-']

line_list = []

for line in lines.split():
    line_list.append(line)

print(line_list)

line_being_scanned = 0
valid_number_sum = 0
for line in line_list:
    for m in re.finditer(r"(\d+)", line):
        number_valid = False
        print(m)
        print(m.group())
        print(m.start())
        print(m.end())

        # links
        try:
            if line[m.start() - 1] in symbols:
                print('links')
                number_valid = True
        except IndexError:
            pass

        # rechts
        try:
            if line[m.end()] in symbols:
                print('rechts ')
                number_valid = True
        except IndexError:
            pass

        # boven
        if line_being_scanned == 0:
            pass
        else:
            print(line_being_scanned)
            for character_index in range(m.start() - 1, m.end() + 1):
                try:
                    print(line_list[line_being_scanned - 1][character_index])
                    if line_list[line_being_scanned - 1][character_index] in symbols:
                        print('boven')
                        number_valid = True
                except IndexError:
                    pass

        # onder
        print(line_being_scanned)
        print(len(line_list))
        print(line)
        if line_being_scanned + 1 == len(line_list):
            pass
        else:
            print(line_being_scanned)
            for character_index in range(m.start() - 1, m.end() + 1):
                try:
                    print(line_list[line_being_scanned + 1][character_index])
                    if line_list[line_being_scanned + 1][character_index] in symbols:
                        number_valid = True
                except IndexError:
                    pass

        if number_valid is True:
            valid_number_sum = valid_number_sum + int(m.group())

    line_being_scanned += 1
print(valid_number_sum)
