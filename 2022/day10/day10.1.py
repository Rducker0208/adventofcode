commands = open('main.txt').read()

cycles_completed = 0
x_values_per_cycle = {}
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

print(signal_strength)