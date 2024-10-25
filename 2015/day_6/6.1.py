instructions = open('main.txt').readlines()

light_status = [['off' for x in range(1000)] for i in range(1000)]

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
                lamp_row[x] = 'on'

    elif instruction == 'off':
        a, b = cords_begin.split(',')
        c, d = cords_end.split(',')

        for i in range(int(a), int(c) + 1):
            lamp_row = light_status[i]

            for x in range(int(b), int(d) + 1):
                lamp_row[x] = 'off'

    else:
        a, b = cords_begin.split(',')
        c, d = cords_end.split(',')

        for i in range(int(a), int(c) + 1):
            lamp_row = light_status[i]

            for x in range(int(b), int(d) + 1):
                if lamp_row[x] == 'off':
                    lamp_row[x] = 'on'
                else:
                    lamp_row[x] = 'off'

on_counter = 0
for row in light_status:
    for light in row:
        if light == 'on':
            on_counter += 1

print(on_counter)

