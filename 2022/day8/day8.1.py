import pprint

trees = open('main.txt').read().splitlines()

trees_count = 0
trees_found = []

for row_number, tree_row in enumerate(trees):
    for tree_number, tree_height in enumerate(tree_row):
        if row_number == 0 or row_number == len(trees) - 1 or tree_number == 0 or tree_number == len(tree_row) - 1:
            trees_count += 1
        else:
            # check boven
            locations_to_check = [trees[y][tree_number] for y in range(row_number)]
            if all(int(height) < int(tree_height) for height in locations_to_check):
                trees_count += 1
                trees_found.append((tree_number, row_number))
                continue

            # check beneden
            locations_to_check = [trees[y][tree_number] for y in range(row_number + 1, len(trees))]
            if all(int(height) < int(tree_height) for height in locations_to_check):
                trees_count += 1
                trees_found.append((tree_number, row_number))
                continue

            # check links
            locations_to_check = [trees[row_number][x] for x in range(tree_number)]
            if all(int(height) < int(tree_height) for height in locations_to_check):
                trees_count += 1
                trees_found.append((tree_number, row_number))
                continue

            # check rechts
            locations_to_check = [trees[row_number][x] for x in range(tree_number + 1, len(tree_row))]
            if all(int(height) < int(tree_height) for height in locations_to_check):
                trees_count += 1
                trees_found.append((tree_number, row_number))
                continue

print(trees_count)
print(trees_found)

