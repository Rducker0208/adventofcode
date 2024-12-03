import re

total = 0

with open("main.txt") as f:
    instructions = f.read()

real_instructions = re.findall(r"mul([(]*\d{1,3},\d{1,3}[)])", instructions)

for instruction in real_instructions:
    digit1, digit2 = eval(instruction)
    total += digit1 * digit2

print(total)