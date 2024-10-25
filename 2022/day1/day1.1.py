CAL_LIST = open('main.txt').read()
elves = CAL_LIST.split('\n\n')

max_calories = 0

for elve in elves:
    calories_value = 0
    calories = elve.split('\n')
    for calorie_count in calories:
        calories_value += int(calorie_count)

    if calories_value > max_calories:
        max_calories = calories_value

print(max_calories)
