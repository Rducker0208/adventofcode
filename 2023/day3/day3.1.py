import re

lines = open('main.txt').read()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['@', '#', '$', '%', '&', '*', '=', '_', '+', '/', '-']

line_list = []

for line in lines.split():
    line_list.append(line)

line_being_scanned = 0
valid_number_sum = 0
for line in line_list:
    for m in re.finditer(r"(\d+)", line):
        number_valid = False

        # links
        try:
            if line[m.start() - 1] in symbols:
                number_valid = True
        except IndexError:
            pass

        # rechts
        try:
            if line[m.end()] in symbols:
                number_valid = True
        except IndexError:
            pass

        # boven
        if line_being_scanned == 0:
            pass
        else:
            for character_index in range(m.start() - 1, m.end() + 1):
                try:
                    if line_list[line_being_scanned - 1][character_index] in symbols:
                        number_valid = True
                except IndexError:
                    pass

        # onder
        if line_being_scanned + 1 == len(line_list):
            pass
        else:
            for character_index in range(m.start() - 1, m.end() + 1):
                try:
                    if line_list[line_being_scanned + 1][character_index] in symbols:
                        number_valid = True
                except IndexError:
                    pass

        if number_valid is True:
            valid_number_sum = valid_number_sum + int(m.group())

    line_being_scanned += 1
print(valid_number_sum)
