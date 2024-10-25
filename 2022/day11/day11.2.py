import copy
import pprint
import math

INPUT = open('main.txt').read()
monkeys = {}
runs = {}
current_monkey = None

for line in INPUT.splitlines():
    if line.startswith('Monkey'):
        current_monkey = line.split()[1][:-1]
        monkeys[current_monkey] = {}
        runs[current_monkey] = 0

    elif line.startswith('  Starting items:'):
        monkeys[current_monkey]['starting_items'] = list(map(int, line.replace(',', '').split()[2:]))

    elif line.startswith('  Operation:'):
        monkeys[current_monkey]['operation'] = line.split()[1:]

    elif line.startswith('  Test'):
        monkeys[current_monkey]['test_statement'] = line.split()[1:]

    else:
        if 'testresults' not in monkeys[current_monkey].keys():
            monkeys[current_monkey]['testresults'] = {True: line.split()[2:]}
        elif 'false' in line:
            monkeys[current_monkey]['testresults'][False] = line.split()[2:]


mod = math.lcm(*[int(test_loc['test_statement'][-1]) for test_loc in monkeys.values()])

for _ in range(10000):
    for monkey, monkey_values in monkeys.items():
        operation = monkey_values['operation']
        test_case = monkey_values['test_statement']
        test_results = monkey_values['testresults']
        for item in monkey_values['starting_items']:
            original_value = copy.deepcopy(item)
            runs[monkey] += 1
            if '*' in operation:
                if operation.count('old') == 2:
                    item **= 2
                else:
                    item *= int(operation[-1])
            else:
                item += int(operation[-1])

            item %= mod

            if item % int(test_case[-1]) == 0:
                monkeys[test_results[True][-1]]['starting_items'].append(item)
                # print(f'item: {original_value} passed sending to: {test_results[True][-1]}')

            else:
                monkeys[test_results[False][-1]]['starting_items'].append(item)
                # print(f'item: {original_value} failed sending to: {test_results[False][-1]}')

        monkey_values['starting_items'] = []


num_list = list(runs.values())
max_1 = max(num_list)
num_list.remove(max_1)
max_2 = max(num_list)

print(max_1 * max_2)


