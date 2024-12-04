locations_of_x = []
xmas_count = 0

with open('main.txt', 'r') as f:
    plot = [list(x) for x in f.read().splitlines()]

# // Find all appearances of X
for index, row in enumerate(plot):
    for i, char in enumerate(row):
        if char == 'X':
            locations_of_x.append((index, i))

print(locations_of_x)

# // Go through every X's neighbours
for location in locations_of_x:

    # // Horizontal to right
    if location[1] <= len(plot) - 4:
        if plot[location[0]][location[1] + 1] == "M" and plot[location[0]][location[1] + 2] == "A" and plot[location[0]][location[1] + 3] == "S":
            xmas_count += 1

    # // Horizontal to left
    if location[1] >= 3:
        if plot[location[0]][location[1] - 1] == "M" and plot[location[0]][location[1] - 2] == "A" and plot[location[0]][location[1] - 3] == "S":
            xmas_count += 1

    # // Vertical to bottom
    if location[0] <= len(plot) - 4:
        if plot[location[0] + 1][location[1]] == "M" and plot[location[0] + 2][location[1]] == "A" and plot[location[0] + 3][location[1]] == "S":
            xmas_count += 1

    # // Vertical to top
    if location[0] >= 3:
        if plot[location[0] - 1][location[1]] == "M" and plot[location[0] - 2][location[1]] == "A" and plot[location[0] - 3][location[1]] == "S":
            xmas_count += 1

    # // Diagonal to top-left
    if location[0] >= 3 and location[1] >= 3:
        if plot[location[0] - 1][location[1] - 1] == "M" and plot[location[0] - 2][location[1] - 2] == "A" and plot[location[0] - 3][location[1] - 3] == "S":
            xmas_count += 1

    # // Diagonal to top-right
    if location[0] >= 3 and location[1] <= len(plot) - 4:
        if plot[location[0] - 1][location[1] + 1] == "M" and plot[location[0] - 2][location[1] + 2] == "A" and plot[location[0] - 3][location[1] + 3] == "S":
            xmas_count += 1

    # // Diagonal to bottom-left
    if location[0] <= len(plot) - 4 and location[1] >= 3:
        if plot[location[0] + 1][location[1] - 1] == "M" and plot[location[0] + 2][location[1] - 2] == "A" and plot[location[0] + 3][location[1] - 3] == "S":
            xmas_count += 1

    # // Diagonal to bottom-right
    if location[0] <= len(plot) - 4 and location[1] <= len(plot) - 4:
        if plot[location[0] + 1][location[1] + 1] == "M" and plot[location[0] + 2][location[1] + 2] == "A" and plot[location[0] + 3][location[1] + 3] == "S":
            xmas_count += 1

print(xmas_count)