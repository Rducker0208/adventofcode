import math
import pprint

trees = open('main.txt').read().splitlines()

max_score = 0

for row_number, tree_row in enumerate(trees):
    for tree_number, tree_height in enumerate(tree_row):
        scene_scores = []

        # // boven
        if row_number == 0:
            scene_scores.append(0)
        else:
            locations_to_check = [trees[y][tree_number] for y in range(row_number)]
            locations_to_check.reverse()
            lowest_index = math.inf
            for height in range(int(tree_height), 10):
                if int(height) >= int(tree_height) and str(height) in locations_to_check:
                    new_index = locations_to_check.index(str(height)) + 1
                    if new_index < lowest_index:
                        lowest_index = new_index
            if lowest_index == math.inf:
                scene_scores.append(len(locations_to_check))
            else:
                scene_scores.append(lowest_index)

        # // onder
        if row_number == len(trees) - 1:
            scene_scores.append(0)
        else:
            locations_to_check = [trees[y][tree_number] for y in range(row_number + 1, len(trees))]
            lowest_index = math.inf
            for height in range(int(tree_height), 10):
                if int(height) >= int(tree_height) and str(height) in locations_to_check:
                    new_index = locations_to_check.index(str(height)) + 1
                    if new_index < lowest_index:
                        lowest_index = new_index
            if lowest_index == math.inf:
                scene_scores.append(len(locations_to_check))
            else:
                scene_scores.append(lowest_index)

        # // links
        if tree_number == 0:
            scene_scores.append(0)
        else:
            locations_to_check = [trees[row_number][x] for x in range(tree_number)]
            locations_to_check.reverse()
            lowest_index = math.inf
            for height in range(int(tree_height), 10):
                if int(height) >= int(tree_height) and str(height) in locations_to_check:
                    new_index = locations_to_check.index(str(height)) + 1
                    if new_index < lowest_index:
                        lowest_index = new_index

            if lowest_index == math.inf:
                scene_scores.append(len(locations_to_check))
            else:
                scene_scores.append(lowest_index)

        # // rechts
        if tree_number == len(tree_row) - 1:
            scene_scores.append(0)
        else:
            locations_to_check = [trees[row_number][x] for x in range(tree_number + 1, len(tree_row))]
            lowest_index = math.inf
            for height in range(int(tree_height), 10):
                if int(height) >= int(tree_height) and str(height) in locations_to_check:
                    new_index = locations_to_check.index(str(height)) + 1
                    if new_index < lowest_index:
                        lowest_index = new_index

            if lowest_index == math.inf:
                scene_scores.append(len(locations_to_check))
            else:
                scene_scores.append(lowest_index)

        scene_score = math.prod(scene_scores)
        if scene_score > max_score:
            max_score = scene_score

print(max_score)