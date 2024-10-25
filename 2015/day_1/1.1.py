instructions = open('main.txt').read()
current_floor = 0

for char in instructions:
    if char == '(':
        current_floor += 1
    else:
        current_floor -= 1

print(current_floor)
