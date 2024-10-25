import string
strings = open('main.txt').read().splitlines()
valid_words = 0

for santa_string in strings:
    double_letter = False
    double_combo = False

    # // find double pair
    for i in range(len(santa_string) - 1):
        combo = santa_string[i:i+2]

        if santa_string.count(combo) > 1:
            double_combo = True

    # // find double letter
    for i in range(len(santa_string) - 2):
        if santa_string[i] == santa_string[i + 2]:
            double_letter = True

    if double_letter and double_combo:
        valid_words += 1

print(valid_words)

