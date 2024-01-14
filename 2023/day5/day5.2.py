INPUT = open('main.txt').read()


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
        destination, source, range_length = number_row.split(' ')
        difference = int(destination) - int(source)
        num_range = (int(source), int(source) + int(range_length), difference)
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

    # // alle destination ranges
    for rule_low, rule_high, rule_difference in destination_list:

        # // voeg nieuwe ranges om te checken en ranges de zijn opgeslagen vanuit de vorige rule samen in 1 list
        ranges_to_check = []
        ranges_to_check.extend(save_for_next_rule_list)
        save_for_next_rule_list = []

        # // check voor overlaps en save de overgbleven source in de save_for_next_rule_list
        for source_low, source_high in ranges_to_check:

            # mogelijkheid 1.1
            if source_low == rule_low and source_high > rule_high:
                intersection = (rule_low + rule_difference, rule_high + rule_difference)
                new_ranges.append(intersection)
                remainder_of_source = (rule_high, source_high)
                save_for_next_rule_list.append(remainder_of_source)

            # mogelijkheid 1.2
            elif rule_low > source_low and rule_high < source_high:
                intersection = (rule_low + rule_difference, rule_high + rule_difference)
                new_ranges.append(intersection)
                remainder_of_source_1 = (source_low, rule_low)
                remainder_of_source_2 = (rule_high, source_high)
                save_for_next_rule_list.append(remainder_of_source_1)
                save_for_next_rule_list.append(remainder_of_source_2)

            # mogelijkheid 1.3
            elif rule_low > source_low and rule_high == source_high:
                intersection = (rule_low + rule_difference, rule_high + rule_difference)
                new_ranges.append(intersection)
                remainder_of_source = (source_low, rule_low)
                save_for_next_rule_list.append(remainder_of_source)

            # mogelijkheid 2
            elif source_low > rule_low and source_high < rule_high:
                intersection = (source_low + rule_difference, source_high + rule_difference)
                new_ranges.append(intersection)

            # mogelijkheid 3
            elif source_low == rule_low and source_high < rule_high:
                intersection = (source_low + rule_difference, source_high + rule_difference)
                new_ranges.append(intersection)

            # mogelijkheid 4
            elif source_low > rule_low and source_high == rule_high:
                intersection = (source_low + rule_difference, source_high + rule_difference)
                new_ranges.append(intersection)

            # mogelijkheid 5
            elif source_low < rule_low < source_high < rule_high:
                intersection = (rule_low + rule_difference, source_high + rule_difference)
                new_ranges.append(intersection)
                remainder_of_source = (source_low, rule_low)
                save_for_next_rule_list.append(remainder_of_source)

            # mogelijkheid 6
            elif source_high > rule_high > source_low > rule_low:
                intersection = (source_low + rule_difference, rule_high + rule_difference)
                new_ranges.append(intersection)
                remainder_of_source = (rule_high, source_high)
                save_for_next_rule_list.append(remainder_of_source)

            # mogelijkheid 7 (geen interceptie)
            else:
                save_for_next_rule_list.append((source_low, source_high))

    new_ranges.extend(save_for_next_rule_list)
    return new_ranges


for seed_range in seed_ranges:
    source_ranges = [seed_range]
    find_seed_endpoint(source_ranges)

print(min(final_list)[0])