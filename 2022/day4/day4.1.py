INPUT = open('main.txt').read()

pairs = 0

for line in INPUT.splitlines():
    elf_1, elf_2 = line.split(',')

    elf_1_l = int(elf_1.split('-')[0])
    elf_1_h = int(elf_1.split('-')[1])

    elf_2_l = int(elf_2.split('-')[0])
    elf_2_h = int(elf_2.split('-')[1])

    if elf_2_l <= elf_1_l and elf_2_h >= elf_1_h or elf_1_l <= elf_2_l and elf_1_h >= elf_2_h:
        pairs += 1

print(pairs)