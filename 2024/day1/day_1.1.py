list1 = []
list2 = []
dif = 0

for line in open("main.txt").readlines():
    x, y = line.split()
    list1.append(int(x))
    list2.append(int(y))

for x, y in zip(sorted(list1), sorted(list2)):
    dif += abs(x - y)

print(dif)