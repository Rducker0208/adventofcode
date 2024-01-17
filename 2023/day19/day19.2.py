import copy
from intersectlib import find_intersection_and_remainders

INPUT = open('main.txt').read()
workflows_input = INPUT.split('\n\n')[0]

total = 0
workflow_dict = {}
workflows_possible_ranges = {'A': [], 'R': []}
test_dict = {}
accepted_ranges_list = []
rejected_ranges_list = []

for full_rule in workflows_input.splitlines():
    name, rule = full_rule[:-1].split('{')
    workflow_dict[name] = rule
    workflows_possible_ranges[name] = []


workflows_possible_ranges['in'].append({'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)})

# // blijf doorgaan totdat alle ranges zijn geaccept of gereject
while any(a != [] for a in workflows_possible_ranges.values()):

    # // ga door alle workflows
    for workflow, possible_ranges in workflows_possible_ranges.items():

        # // check of je in deze workflows nog ranges moet checken
        if possible_ranges:
            rules = workflow_dict[workflow]

            # // zo ja loop door al deze ranges
            for current_range in possible_ranges:
                workflows_possible_ranges[workflow].remove(current_range)

                # // loop door alle rules om te kijken waar de ranges heen moeten
                for rule in rules.split(','):
                    value_to_check = rule[0]

                    if rule == 'A':
                        dict_copy = copy.deepcopy(current_range)
                        accepted_ranges_list.append(dict_copy)

                    elif rule == 'R':
                        dict_copy = copy.deepcopy(current_range)
                        rejected_ranges_list.append(dict_copy)

                    elif '<' not in rule and '>' not in rule:
                        dict_copy = copy.deepcopy(current_range)
                        workflows_possible_ranges[rule].append(dict_copy)

                    elif '<' in rule:

                        # // verzamel welk getal er is om te checken en waar de valid ranges naartoe moeten
                        last_value = rule.split('<')[1].split(':')[0]
                        intersection_destination = rule.split(':')[1]

                        # // verzamel source en dest voor de find functie
                        source = current_range[value_to_check]
                        dest = (1, int(last_value))

                        # // verzamel deze en pas ze aan vanwege de non-inclusive <
                        intersection, remainder = find_intersection_and_remainders(source, dest)
                        intersection = (intersection[0], intersection[1] - 1)

                        # // move intersection naar bestemming
                        if intersection:
                            current_range[value_to_check] = intersection
                            dict_copy = copy.deepcopy(current_range)

                            if intersection_destination == 'A':
                                accepted_ranges_list.append(dict_copy)

                            elif intersection_destination == 'R':
                                rejected_ranges_list.append(dict_copy)

                            else:
                                workflows_possible_ranges[intersection_destination].append(dict_copy)

                        # // bewaar remainders
                        if remainder:
                            current_range[value_to_check] = remainder[0]

                    elif '>' in rule:

                        # // verzamel welk getal er is om te checken en waar de valid ranges naartoe moeten
                        last_value = rule.split('>')[1].split(':')[0]
                        intersection_destination = rule.split(':')[1]

                        # // verzamel source en dest voor de find functie
                        source = current_range[value_to_check]
                        dest = (int(last_value), 4000)

                        # // verzamel deze en pas ze aan vanwege de non-inclusive >
                        intersection, remainder = find_intersection_and_remainders(source, dest)
                        intersection = (intersection[0] + 1, intersection[1])

                        # // move intersection naar bestemming
                        if intersection:
                            current_range[value_to_check] = intersection
                            dict_copy = copy.deepcopy(current_range)

                            if intersection_destination == 'A':
                                accepted_ranges_list.append(dict_copy)

                            elif intersection_destination == 'R':
                                rejected_ranges_list.append(dict_copy)

                            else:
                                workflows_possible_ranges[intersection_destination].append(dict_copy)

                        # // bewaar remainders
                        if remainder:
                            current_range[value_to_check] = remainder[0]


for item in accepted_ranges_list:
    total += (item['x'][1] - item['x'][0] + 1) * (item['m'][1] - item['m'][0] + 1) * (item['a'][1] - item['a'][0] + 1) * (item['s'][1] - item['s'][0] + 1)


print(total)
