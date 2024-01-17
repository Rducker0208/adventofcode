import copy

INPUT = open('main.txt').read()

pulse_dict = {}
and_locations = {}
location_info = {}
status_info = {}
watch_locations_dict = {}
button_presses = 1
high_pulses, total_pulses, low_pulses = (0, 0, 0)

new_pulses = []
unmapped_locations = []

for raw_input_line in INPUT.splitlines():
    name, _, *destinations = raw_input_line.split(' ')
    if not name == 'broadcaster':
        location_info[name[1:]] = (name[0], [i.replace(',', '') for i in destinations])
        if name[0] == '%':
            status_info[name[1:]] = 'off'
        elif name[0] == '&':
            status_info[name[1:]] = 'low'
    else:
        location_info[name] = (None, [i.replace(',', '') for i in destinations])
        status_info[name] = None

for name, destinations in location_info.items():
    for item in destinations[1]:
        if item not in location_info.keys():
            unmapped_locations.append(item)

for loc in unmapped_locations:
    location_info[loc] = ('-', '-')
    status_info[loc] = None

# // verzamel & locaties
for name, status in status_info.items():
    if status == 'low':
        status_info[name] = []
        and_locations[name] = []

for name, info in location_info.items():
    for dest in info[1]:
        if dest in and_locations.keys():
            status_info[dest].append((name, 'low'))

original_dict = copy.deepcopy(status_info)

pulses_to_send = [('broadcaster', 'low', i) for i in location_info['broadcaster'][1]]

high_pulses, total_pulses, low_pulses = (0, 0, 0)

for _ in range(1000):
    while True:
        for pulse in pulses_to_send:
            origin = pulse[0]
            pulse_type = pulse[1]
            destinations = [pulse[2]]

            for destination in destinations:
                if pulse_type == 'high':
                    high_pulses += 1
                else:
                    low_pulses += 1

                destination_info = location_info[destination]
                destination_status = status_info[destination]

                if destination_info[0] == '%':
                    if pulse_type == 'low':
                        if destination_status == 'off':
                            status_info[destination] = 'on'
                            new_pulses.extend([(pulse[2], 'high', i) for i in destination_info[1]])
                        elif destination_status == 'on':
                            status_info[destination] = 'off'
                            new_pulses.extend([(pulse[2], 'low', i) for i in destination_info[1]])

                elif destination_info[0] == '&':
                    watch_locations = status_info[destination]
                    for loc_tuple in watch_locations:
                        if loc_tuple[0] == origin:
                            status_info[destination].remove(loc_tuple)
                            status_info[destination].append((origin, pulse_type))

                    if all(watch_tuple[1] == 'high' for watch_tuple in status_info[destination]):
                        new_pulses.extend([(pulse[2], 'low', dest) for dest in destination_info[1]])

                    else:
                        new_pulses.extend([(pulse[2], 'high', dest) for dest in destination_info[1]])

        if new_pulses:
            pulses_to_send = copy.deepcopy(new_pulses)
            new_pulses = []
        else:
            pulses_to_send = ([('broadcaster', 'low', i) for i in location_info['broadcaster'][1]])
            button_presses += 1
            break

print((low_pulses + 1000) * high_pulses)