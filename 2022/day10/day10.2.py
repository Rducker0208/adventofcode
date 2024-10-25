commands = open('main.txt').read()

cycles_completed = 0
x_values_per_cycle = {0: 1}
signal_strength = 0
x = 1

for command in commands.splitlines():
    if command == 'noop':
        cycles_completed += 1
    else:
        V = command.split()[-1]
        x_values_per_cycle[cycles_completed + 1] = x
        cycles_completed += 2
        x += int(V)
    x_values_per_cycle[cycles_completed] = x

for cycle_num, x_value in x_values_per_cycle.items():
    if (cycle_num - 20) % 40 == 0:
        signal_strength += cycle_num * x_values_per_cycle[cycle_num - 1]

rows_needed = int(cycles_completed / 40)


times_ran = 0
for i in range(rows_needed):
    cycle = 0
    crt_row = ''
    for _ in range(40):
        sprite_middle = x_values_per_cycle[cycle + 40 * times_ran]
        locations_to_draw = [sprite_middle - 1, sprite_middle, sprite_middle + 1]
        pixel_pos = cycle
        cycle += 1
        if pixel_pos in locations_to_draw:
            crt_row += '#'
        else:
            crt_row += '.'

    print(crt_row)
    times_ran += 1



