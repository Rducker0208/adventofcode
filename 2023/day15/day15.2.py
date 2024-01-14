import aoc_lube


INPUT = aoc_lube.fetch(year=2023, day=15)

letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
actions = []
boxes = {}
labels_in_boxes = {}

for i in range(256):
    boxes[i] = []
    labels_in_boxes[i] = []


# verzamel data over letters, actie die uitgevoerd moet worden en lens
for item in INPUT.split(','):
    letters = None
    seperator = None
    focal_strength = None
    for character_index, character in enumerate(item):
        print(character)
        if character not in letter_list:
            letters = item[:character_index]
            seperator = character
            break

    if seperator == '=':
        focal_strength = item[-1]

    actions.append((letters, seperator, focal_strength))

print(actions)


def hash_algorithm(string):
    value = 0
    string_letters = list(string)
    for letter in string_letters:
        value += ord(letter)
        value *= 17
        value = value % 256
    return value


for action in actions:
    label = action[0]
    action_operator = action[1]
    focal_strength = action[2]
    box_to_change = hash_algorithm(label)
    if action_operator == '-':
        for item in boxes[box_to_change]:
            if item[0] == label:
                boxes[box_to_change].remove(item)

    elif action_operator == '=':
        for index, item in enumerate(boxes[box_to_change]):
            if item[0] == label:
                boxes[box_to_change].pop(index)
                boxes[box_to_change].insert(index, (label, focal_strength))
                break
        else:
            boxes[box_to_change].append((label, focal_strength))

total_sum = 0

for box_number, box_content in boxes.items():
    if not box_content:
        continue
    else:
        for item_index, item in enumerate(box_content):
            sum_to_add = (box_number + 1) * (item_index + 1) * int(item[1])
            total_sum += sum_to_add
            print(f'{box_number, item_index + 1}: {sum_to_add}')

print(total_sum)

