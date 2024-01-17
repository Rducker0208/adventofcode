INPUT = open('main.txt').read()

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

    if status == 'accepted':
        xmas_list = [int(x), int(m), int(a), int(s)]
        final_sum += sum(xmas_list)

print(final_sum)