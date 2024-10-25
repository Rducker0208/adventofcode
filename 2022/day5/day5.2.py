crates, instructions = open('main.txt').read().split('\n\n')
crate_rows = crates[:-1].splitlines()

stacks = {int(stack_id): [] for stack_id in crates.splitlines()[-1].split()}
final_message = ''

for row in crate_rows:
    i = 0
    step = 0
    for _ in range(len(stacks.keys())):
        step += 1
        if '[' in row[i:i+3] and ']' in row[i:i+3]:
            stacks[step].append(row[i:i+3])
        i += 4


for instruction in instructions.splitlines():
    amount_to_move = instruction.split()[1]
    source = instruction.split()[3]
    destination = instruction.split()[5]

    crates_to_move = stacks[int(source)][0: int(amount_to_move)]
    for item in crates_to_move:
        stacks[int(source)].remove(item)
    for item in reversed(crates_to_move):
        stacks[int(destination)].insert(0, item)

for stack, crates in stacks.items():
    crate_on_top = crates[0]
    message_on_crate = crate_on_top[1]
    final_message += message_on_crate

print(final_message)