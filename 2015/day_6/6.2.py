instructions = open('main.txt').readlines()

light_status = [[0 for x in range(1000)] for i in range(1000)]

for line in instructions:
    if 'toggle' in line:
        instruction, cords_begin, _, cords_end = line.strip().split()
    else:
        _, instruction, cords_begin, _, cords_end = line.strip().split()

    if instruction == 'on':
        a, b = cords_begin.split(',')
        c, d = cords_end.split(',')

        for i in range(int(a), int(c) + 1):
            lamp_row = light_status[i]

            for x in range(int(b), int(d) + 1):
                lamp_row[x] += 1

    elif instruction == 'off':
        a, b = cords_begin.split(',')
        c, d = cords_end.split(',')

        for i in range(int(a), int(c) + 1):
            lamp_row = light_status[i]

            for x in range(int(b), int(d) + 1):
                if lamp_row[x] > 0:
                    lamp_row[x] -= 1

    else:
        a, b = cords_begin.split(',')
        c, d = cords_end.split(',')

        for i in range(int(a), int(c) + 1):
            lamp_row = light_status[i]

            for x in range(int(b), int(d) + 1):
                lamp_row[x] += 2


total_brightness = 0
for row in light_status:
    for light in row:
        total_brightness += light


print(total_brightness)


