import copy
import pprint

INPUT = open('main.txt').read()

directories = {'/': {}}
sizes = {'/': 0}
current_location_list = ['/']

final_sum = 0


def get_current_location(loc_dict, loc_list):
    location_list = copy.deepcopy(loc_list)
    for item in location_list:
        loc_dict = loc_dict[item]

    return loc_dict


for index, command in enumerate(INPUT.splitlines()):
    if command.startswith('$'):
        if command.split()[1] == 'ls':
            pass

        else:
            dest = command.split()[2]
            if dest == '/':
                current_location_list = ['/']
            elif dest == '..':
                current_location_list.pop()
            else:
                old_loc = current_location_list[-1]
                current_location_list.append(f'{old_loc}_/{dest}')
                if current_location_list[-1] not in sizes:
                    sizes[f'{old_loc}_/{dest}'] = 0

    else:
        if command.startswith('dir'):
            pass
        else:
            for item in current_location_list:
                print(item)
                sizes[item] += int(command.split()[0])


space_used = 70000000 - sizes['/']
space_to_be_cleared = 30000000 - space_used
print(space_to_be_cleared)


print(min([size for size in sizes.values() if size > space_to_be_cleared]))