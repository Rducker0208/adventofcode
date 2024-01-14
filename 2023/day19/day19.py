import aoc_lube
from pprint import pprint

# INPUT = """px{a<2006:qkq,m>2090:A,rfg}
# pv{a>1716:R,A}
# lnx{m>1548:A,A}
# rfg{s<537:gd,x>2440:R,A}
# qs{s>3448:A,lnx}
# qkq{x<1416:A,crn}
# crn{x>2662:A,R}
# in{s<1351:px,qqz}
# qqz{s>2770:qs,m<1801:hdj,R}
# gd{a>3333:R,R}
# hdj{m>838:A,pv}
#
# {x=787,m=2655,a=1222,s=2876}
# {x=1679,m=44,a=2067,s=496}
# {x=2036,m=264,a=79,s=2244}
# {x=2461,m=1339,a=466,s=291}
# {x=2127,m=1623,a=2188,s=1013}"""

# INPUT = aoc_lube.fetch(year=2023.1, day=19)
with open('../../day19.txt', 'r') as f:
    INPUT = f.read()

# print(INPUT)

rules, parts = INPUT.split('\n\n')
workflow_dict = {}
accepted_parts = []
rejected_parts = []
final_sum = 0

for item in rules.splitlines():
    name, rule = item.split('{')
    rule.replace('}', '')
    workflow_dict[name] = list(rule[:-1].split(','))


for part in parts.splitlines():
    part_split = part[:-1].split('=')
    x = part_split[1].split(',')[0]
    m = part_split[2].split(',')[0]
    a = part_split[3].split(',')[0]
    s = part_split[4]
    status = None
    current_workflow = 'in'

    while status is None:
        current_workflow_rules = workflow_dict[current_workflow]

        for workflow_rule in current_workflow_rules[:-1]:
            print(workflow_rule)
            value_to_check = workflow_rule[0]
            condition = workflow_rule[1]
            number, new_workflow = workflow_rule[2:].split(':')

            if value_to_check == 'x':
                value_to_check = x
            elif value_to_check == 'm':
                value_to_check = m
            elif value_to_check == 'a':
                value_to_check = a
            else:
                value_to_check = s

            if condition == '>':
                if int(value_to_check) > int(number):
                    if new_workflow == 'A':
                        status = 'accepted'
                        break
                    elif new_workflow == 'R':
                        status = 'rejected'
                        break
                    else:
                        current_workflow = new_workflow
                        break

            elif condition == '<':
                if int(value_to_check) < int(number):
                    if new_workflow == 'A':
                        status = 'accepted'
                        break
                    elif new_workflow == 'R':
                        status = 'rejected'
                        break
                    else:
                        current_workflow = new_workflow
                        break

        else:
            if current_workflow_rules[-1] == 'A':
                status = 'accepted'
                break
            elif current_workflow_rules[-1] == 'R':
                status = 'rejected'
                break
            else:
                current_workflow = current_workflow_rules[-1]

    print(f'part: {part}\n'
          f'status: {status}')
    if status == 'accepted':
        xmas_list = [int(x), int(m), int(a), int(s)]
        final_sum += sum(xmas_list)

print(final_sum)