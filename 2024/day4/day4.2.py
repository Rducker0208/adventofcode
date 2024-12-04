import pprint

locations_of_a = []
xmas_count = 0

# // Create a 2d plot
with open('main.txt', 'r') as f:
    plot = [list(x) for x in f.read().splitlines()]

# // Pad the plot
for line in plot:
    line.insert(0, "|")
    line.append("|")

plot.append(list("-" * len(plot[0])))
plot.insert(0, list("-" * len(plot[0])))

# // Find all appearances of A
for index, row in enumerate(plot):
    for i, char in enumerate(row):
        if char == 'A':
            locations_of_a.append((index, i))

# // Go through every A to find X-mas's
for location in locations_of_a:
    req1 = False
    req2 = False

    # // Find out what letter A's diagonal neighbours are
    top_left = plot[location[0] - 1][location[1] - 1]
    bottom_right = plot[location[0] + 1][location[1] + 1]

    top_right = plot[location[0] - 1][location[1] + 1]
    bottom_left = plot[location[0] + 1][location[1] - 1]

    # // Check for an Xmas
    if top_left == "M" and bottom_right == "S":
        req1 = True
    elif top_left == "S" and bottom_right == "M":
        req1 = True

    if top_right == "M" and bottom_left == "S":
        req2 = True
    elif top_right == "S" and bottom_left == "M":
        req2 = True

    xmas_count += req1 * req2

print(xmas_count)