dimension_list = open('main.txt').readlines()
total_packaging = 0

for dimensions in dimension_list:
    length, width, height = map(int, dimensions.split('x'))
    sides = [2 * length * width, 2 * width * height, 2 * height * length]
    total_packaging += sum(sides) + (min(sides) // 2)

print(total_packaging)

