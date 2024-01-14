import aoc_lube

# values = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45""".splitlines()

values = aoc_lube.fetch(year=2023, day=9).splitlines()
print(values)

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
        # print(difference)
        difference_index += 1
    row_number += 1

    # print(difference_list)
    # print(row_number)
    # print(rows_library)
    # quit()

    while True:
        if all(difference == 0 for difference in difference_list):
            difference_list.append(0)
            # print('in loop')
            while True:
                print('while loop___________')
                print(difference_list)
                print(row_number)
                if row_number - 2 > 0:
                    print('if______________-')
                    last_difference_list = rows_library[row_number - 2]
                    last_difference_list.append(last_difference_list[-1] + rows_library[row_number - 1][-1])
                    print(last_difference_list)
                    row_number -= 1
                else:
                    print('else_____________')
                    rows_library[0].append(rows_library[0][-1] + rows_library[1][-1])
                    total += rows_library[0][-1]
                    break
            print(rows_library)
            break

        else:
            difference_index = 1
            new_difference_list = []

            while True:
                if difference_index == len(difference_list):
                    break
                # print(difference_list)
                # print(difference_index)
                difference = difference_list[difference_index] - difference_list[difference_index - 1]
                new_difference_list.append(difference)
                rows_library[row_number] = new_difference_list
                difference_index += 1
            row_number += 1
            difference_list = new_difference_list

    # quit()

print(total)






