import aoc_lube

# INPUT = 'rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7'
# INPUT = 'qp'
INPUT = aoc_lube.fetch(year=2023, day=15)

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

print(letter_values)

for letter_value in letter_values:
    total_sum += letter_value

print(total_sum)

