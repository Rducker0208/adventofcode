strings = open('main.txt').readlines()
valid_words = 0

for string in strings:
    vowel_count = 0
    string_valid = True
    double_letter = False

    # // Go through all the letters to check for illegal combinations and double letters
    for index, letter in enumerate(string):
        if letter == 'a':
            if string[index + 1] == 'b':
                string_valid = False
                break

            elif string[index + 1] == 'a':
                double_letter = True

        elif letter == 'c':
            if string[index + 1] == 'd':
                string_valid = False
                break

            elif string[index + 1] == 'c':
                double_letter = True

        elif letter == 'p':
            if string[index + 1] == 'q':
                string_valid = False
                break

            elif string[index + 1] == 'p':
                double_letter = True

        elif letter == 'x':
            if string[index + 1] == 'y':
                string_valid = False
                break

            elif string[index + 1] == 'x':
                double_letter = True

        try:
            if string[index + 1] == letter:
                double_letter = True
        except IndexError:
            pass

    for letter in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += string.count(letter)

    if string_valid and double_letter and vowel_count >= 3:
        valid_words += 1

print(valid_words)




