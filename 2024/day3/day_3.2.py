import re
total = 0

real_instructions = []

with open("main.txt") as f:
    instructions = f.read()

# // find all mul instructions
real_instuctions_raw = re.findall(r"mul([(]*\d{1,3},\d{1,3}[)])", instructions)
real_instuctions_indexes = [(m.start(0), m.end(0)) for m in re.finditer(r"mul([(]*\d{1,3},\d{1,3}[)])", instructions)]

for instruction, indexes in zip(real_instuctions_raw, real_instuctions_indexes):
    real_instructions.append((instruction, indexes[0]))

# // find all do instructions
do_instructions_indexes = [m.start(0) for m in re.finditer(r"do[(][)]", instructions)]

# // find all don't instructions
dont_instructions_indexes = [m.start(0) for m in re.finditer(r"don't[(][)]", instructions)]

# // create a dict with enabled/disabled zones
current_status = 'enabled'
enabled_zones = {}

for index in range(len(instructions)):
    if current_status == 'enabled':
        if index in dont_instructions_indexes:
            current_status = 'disabled'
            enabled_zones[index] = 'disabled'
        else:
            enabled_zones[index] = 'enabled'

    else:
        if index in do_instructions_indexes:
            current_status = 'enabled'
            enabled_zones[index] = 'enabled'
        else:
            enabled_zones[index] = 'disabled'

for instruction, index in real_instructions:
    if enabled_zones[index] == 'enabled':
        digit1, digit2 = eval(instruction)
        total += digit1 * digit2

print(total)