INPUT = open('main.txt').read()

values = INPUT.split(',')

letter_values = []

total_sum = 0

for value in values:
    letter_value = 0
    letters = list(value)
    for letter in letters:
        letter_value += ord(letter)
        letter_value *= 17
        letter_value = letter_value % 256
    letter_values.append(letter_value)

for letter_value in letter_values:
    total_sum += letter_value

print(total_sum)

