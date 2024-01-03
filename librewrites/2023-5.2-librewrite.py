import aoc_lube
import intersectlib

INPUT = aoc_lube.fetch(year=2023, day=5)

maps = []
map_names = []
maps_with_range_dict = {}
location_list = []
new_seed_list = []
final_list = []
loop_Count = 0
seed_ranges = []
new_range = None

# ______________ Data verzameling ______________

split = INPUT.split('\n\n')

# // verzamel seeds
SEED_INFO = split[0]
SEEDS = SEED_INFO.split()
SEEDS.remove('seeds:')

# // verzamel andere paden:
for i in range(1, 8):
    maps.append(split[i])


# // verander seeds in ranges
for seed_index, seed_number in enumerate(SEEDS):
    if len(SEEDS) == 0:
        break
    begin_number = int(SEEDS[0])
    end_number = int(SEEDS[1]) + int(begin_number)
    seed_range = (begin_number, end_number)
    seed_ranges.append(seed_range)
    SEEDS.pop(0)
    SEEDS.pop(0)


# // verander andere maps in ranges
for item in maps:
    ranges = []
    name = item.split(':')[0].split()[0]
    map_numbers = item.split(':')[1]
    for number_row in map_numbers.splitlines()[1:]:
        dest, source, range_length = number_row.split(' ')
        diff = int(dest) - int(source)
        num_range = ((int(source), int(source) + int(range_length)), diff)
        ranges.append(num_range)

    map_names.append(name)
    maps_with_range_dict[name] = ranges


def find_seed_endpoint(ranges_list):

    # // loop door alle maps heen met deze seed
    for map_name, map_with_ranges in maps_with_range_dict.items():
        ranges_list = find_new_ranges(ranges_list, map_with_ranges)
    final_list.extend(ranges_list)


def find_new_ranges(source_list, destination_list):
    save_for_next_rule_list = []
    save_for_next_rule_list.extend(source_list)
    new_ranges = []

    for destination, difference in destination_list:
        ranges_to_check = []
        ranges_to_check.extend(save_for_next_rule_list)
        save_for_next_rule_list = []
        for source_range in ranges_to_check:
            intersection, remainders = intersectlib.find_intersection_and_remainders(source_range, destination)

            if intersection:
                new_ranges.append(intersectlib.transform_existing_intersection(intersection, difference))

            if remainders:
                save_for_next_rule_list.extend(remainders)

    new_ranges.extend(save_for_next_rule_list)
    return new_ranges


for seed_range in seed_ranges:
    source_ranges = [seed_range]
    find_seed_endpoint(source_ranges)

print(min(final_list)[0])