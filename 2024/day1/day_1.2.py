values = {}
list1 = []
sim_score = 0

for line in open("main.txt").readlines():
    x, y = line.split()
    list1.append(x)

    if y in values.keys():
        values[y] += 1
    else:
        values[y] = 1

for number in list1:
    try:
        sim_score += int(number) * values[number]

    except KeyError:
        pass

print(sim_score)