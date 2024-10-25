CAL_LIST = open('main.txt').read()
elves = CAL_LIST.split('\n\n')

cal_list = []

for elve in elves:
    calories_value = 0
    calories = elve.split('\n')
    for calorie_count in calories:
        calories_value += int(calorie_count)

    cal_list.append(calories_value)

max_cals = max(cal_list)
cal_list.remove(max_cals)

second_max = max(cal_list)
cal_list.remove(second_max)

third_max = max(cal_list)

print(max_cals + second_max + third_max)
