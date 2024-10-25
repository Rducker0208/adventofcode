import sys

sys.setrecursionlimit(10 ** 6)

ports = {'b': 956}

instructions: list[str] = open('main.txt').read().splitlines()


def solve_a(instructions_to_a, count):
    new_instructions = []

    for instruction in instructions_to_a:
        if "AND" in instruction:
            origin1, _, origin2, _, destination = instruction.split()

            if origin1 in ports.keys() and origin2 in ports.keys():
                ports[destination] = int(ports[origin1]) & int(ports[origin2])

            elif origin1.isnumeric() and origin2 in ports.keys():
                ports[destination] = int(origin1) & int(ports[origin2])

            elif origin1 in ports.keys() and origin2.isnumeric():
                ports[destination] = int(ports[origin1]) & int(origin2)

            elif origin1.isnumeric() and origin2.isnumeric():
                ports[destination] = int(origin1) & int(origin2)
            else:
                new_instructions.append(instruction)

        elif 'OR' in instruction:
            origin1, _, origin2, _, destination = instruction.split()

            if origin1 in ports.keys() and origin2 in ports.keys():
                ports[destination] = int(ports[origin1]) | int(ports[origin2])

            elif origin1.isnumeric() and origin2 in ports.keys():
                ports[destination] = int(origin1) | int(ports[origin2])

            elif origin1 in ports.keys() and origin2.isnumeric():
                ports[destination] = int(ports[origin1]) | int(origin2)

            elif origin1.isnumeric() and origin2.isnumeric():
                ports[destination] = int(origin1) | int(origin2)
            else:
                new_instructions.append(instruction)

        elif 'NOT' in instruction:
            _, origin, _, destination = instruction.split()

            if origin in ports.keys():
                ports[destination] = (1 << 16) - 1 - int(ports[origin])

            elif origin.isnumeric():
                ports[destination] = (1 << 16) - 1 - int(origin)

            else:
                new_instructions.append(instruction)

        elif 'LSHIFT' in instruction:
            origin, _, number, _, destination = instruction.split()

            if origin in ports.keys():
                ports[destination] = int(ports[origin]) << int(number)

            elif origin.isnumeric():
                ports[destination] = int(origin) << int(number)

            else:
                new_instructions.append(instruction)

        elif 'RSHIFT' in instruction:
            origin, _, number, _, destination = instruction.split()

            if origin in ports.keys():
                ports[destination] = int(ports[origin]) >> int(number)

            elif origin.isnumeric():
                ports[destination] = origin >> int(number)

            else:
                new_instructions.append(instruction)

        else:
            origin, _, destination = instruction.split()
            if destination != 'b':
                if origin in ports.keys():
                    ports[destination] = ports[origin]

                elif origin.isnumeric():
                    ports[destination] = origin

                else:
                    new_instructions.append(instruction)

    if not new_instructions:
        print(ports['a'])
        quit()

    return solve_a(new_instructions, count + 1)


solve_a(instructions, 0)

