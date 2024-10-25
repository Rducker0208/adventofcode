dimension_list = open('main.txt').readlines()
total_packaging = 0

for instructions in dimension_list:
    # // length, width, height
    dimensions = list(map(int, instructions.split('x')))

    # // Calculate ribbon for bow
    total_packaging += dimensions[0] * dimensions[1] * dimensions[2]

    # // Calculate ribbon length for wrapping
    shortest_side = min(dimensions)
    dimensions.remove(shortest_side)
    second_side = min(dimensions)

    total_packaging += 2 * shortest_side + 2 * second_side

print(total_packaging)

