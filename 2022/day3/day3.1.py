import string

rucksacks = open('main.txt').read()

final_val = 0

for rucksack in rucksacks.splitlines():
    compartment_length = int(len(rucksack) / 2)
    compartment_1 = rucksack[:compartment_length]
    compartment_2 = rucksack[compartment_length:]

    for character in compartment_1:
        if character in compartment_2:
            if character in string.ascii_lowercase:
                final_val += ord(character) - 96
            else:
                final_val += ord(character) - 38
            break

print(final_val)

