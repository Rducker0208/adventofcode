values = open('main.txt').read().splitlines()

total = 0
rows_library = {}

for value in values:
    value_history = list(map(int, value.split()))
    rows_library[0] = value_history
    row_number = 1

    difference_index = 1
    difference_list = []

    history_length = len(value_history)

    while True:
        if difference_index == history_length:
            break
        difference = value_history[difference_index] - value_history[difference_index - 1]
        difference_list.append(difference)
        rows_library[row_number] = difference_list
        difference_index += 1
    row_number += 1

    while True:
        if all(difference == 0 for difference in difference_list):
            difference_list.append(0)
            while True:
                if row_number - 2 > 0:
                    last_difference_list = rows_library[row_number - 2]
                    last_difference_list.append(last_difference_list[-1] + rows_library[row_number - 1][-1])
                    print(last_difference_list)
                    row_number -= 1
                else:
                    rows_library[0].append(rows_library[0][-1] + rows_library[1][-1])
                    total += rows_library[0][-1]
                    break
            break

        else:
            difference_index = 1
            new_difference_list = []

            while True:
                if difference_index == len(difference_list):
                    break
                difference = difference_list[difference_index] - difference_list[difference_index - 1]
                new_difference_list.append(difference)
                rows_library[row_number] = new_difference_list
                difference_index += 1
            row_number += 1
            difference_list = new_difference_list

print(total)






