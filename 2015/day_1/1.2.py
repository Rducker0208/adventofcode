instructions = open('main.txt').read()
current_floor = 0

for index, char in enumerate(instructions):
    if char == '(':
        current_floor += 1
    else:
        current_floor -= 1

    if current_floor == -1:
        print(index + 1)
        quit()