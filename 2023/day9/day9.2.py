values = open('main.txt').read().splitlines()

total = 0

# // ga elke lijst met geschiedenis af
for unsplitted_history in values:

    rows_library = {}
    difference_list = []

    # transfer value lijst naar een lijst met integers van de value geschiedenis
    full_value_history = list(map(int, unsplitted_history.split()))

    # // zet originele lijst op plek nul
    row_number = 0
    rows_library[0] = full_value_history

    first_digit = full_value_history[0]

    # // verzamel rows totdat alle nummers 0 zijn en je dus in de laatste row bent
    while True:

        # // als je in de laatste row bent
        if all(history_value == 0 for history_value in difference_list) and difference_list != []:
            rows_library[row_number] = difference_list
            break

        # // zo niet creer dan een nieuwe difference lijst
        else:
            difference_list = []
            value_to_check = 1

            current_list = rows_library[row_number]

            while True:
                # als je item dat je gaat checken na het laatste item uit de lijst komt
                if value_to_check == len(current_list):
                    break

                # bereken verschil tussen twee items
                difference = current_list[value_to_check] - current_list[value_to_check - 1]
                difference_list.append(difference)
                value_to_check += 1
            row_number += 1
            rows_library[row_number] = difference_list
    rows_library[row_number].insert(0, 0)

    while True:
        if row_number == 0:
            total += rows_library[0][0]
            break
        else:
            current_row = rows_library[row_number]
            rows_library[row_number - 1].insert(0, rows_library[row_number - 1][0] - rows_library[row_number][0])
            row_number -= 1

print(total)