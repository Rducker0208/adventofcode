import string

rucksacks = open('main.txt').read()

final_val = 0
rucksack_group_id = 1
i = 1
rucksack_groups = {}

for rucksack in rucksacks.splitlines():
    if i == 1:
        rucksack_groups[rucksack_group_id] = [rucksack]
        i += 1
    elif i == 2:
        rucksack_groups[rucksack_group_id].append(rucksack)
        i += 1
    else:
        rucksack_groups[rucksack_group_id].append(rucksack)
        i = 1
        rucksack_group_id += 1


for rucksack_group in rucksack_groups.values():
    for character in rucksack_group[0]:
        if character in rucksack_group[1] and character in rucksack_group[2]:
            if character in string.ascii_lowercase:
                final_val += ord(character) - 96
            else:
                final_val += ord(character) - 38
            break

print(final_val)
