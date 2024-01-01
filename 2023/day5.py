import aoc_lube
import re
INPUT = aoc_lube.fetch(year=2023, day=5)
# INPUT = """seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4"""

SOIL_DATA = []
FERTILIZER_DATA = []
WATER_DATA = []
LIGHT_DATA = []
TEMPERATURE_DATA = []
HUMIDITY_DATA = []
LOCATION_DATA = []
ALL_DATAS_LIST = [SOIL_DATA, FERTILIZER_DATA, WATER_DATA, LIGHT_DATA, TEMPERATURE_DATA, HUMIDITY_DATA, LOCATION_DATA]

ALL_SOIL_DATA = []
ALL_FERTILIZER_DATA = []
ALL_WATER_DATA = []
ALL_LIGHT_DATA = []
ALL_TEMPERATURE_DATA = []
ALL_HUMIDITY_DATA = []
ALL_LOCATION_DATA = []
ALL_FULL_DATAS_LIST = [ALL_SOIL_DATA, ALL_FERTILIZER_DATA, ALL_WATER_DATA, ALL_LIGHT_DATA, ALL_TEMPERATURE_DATA,
                       ALL_HUMIDITY_DATA, ALL_LOCATION_DATA]

location_list = []

# ______________ Data verzameling ______________

print('_________________seeds_________________')
# // verzamel seeds
SEED_INFO = INPUT.split('seed-to-soil')
SEEDS = SEED_INFO[0].split()
SEEDS.remove('seeds:')

print(SEEDS)

# // Verzamel soil data
SOIL_NUMBERS = INPUT.split(':')[2]
search_mode = 'source'

for number in re.finditer(r'(\d+)', SOIL_NUMBERS):
    if search_mode == 'source':
        SOIL_DATA = []  # noqa
        SOIL_DATA.append(int(number.group()))
        search_mode = 'destination'
    elif search_mode == 'destination':
        SOIL_DATA.append(int(number.group()))
        search_mode = 'range'
    elif search_mode == 'range':
        SOIL_DATA.append(int(number.group()))
        search_mode = 'source'
        ALL_SOIL_DATA.append(SOIL_DATA)

print('___________soil________________')
for PRINT_LIST in ALL_SOIL_DATA:
    print(PRINT_LIST)

# // Verzamel fertilizer data

FERTILZER_NUMBERS = INPUT.split(':')[3]
search_mode = 'source'

for number in re.finditer(r'(\d+)', FERTILZER_NUMBERS):
    if search_mode == 'source':
        FERTILIZER_DATA = []  # noqa
        FERTILIZER_DATA.append(int(number.group()))
        search_mode = 'destination'
    elif search_mode == 'destination':
        FERTILIZER_DATA.append(int(number.group()))
        search_mode = 'range'
    elif search_mode == 'range':
        FERTILIZER_DATA.append(int(number.group()))
        search_mode = 'source'
        ALL_FERTILIZER_DATA.append(FERTILIZER_DATA)

print('___________fertilizer________________')
for PRINT_LIST in ALL_FERTILIZER_DATA:
    print(PRINT_LIST)

# // Verzamel water data
WATER_NUMBERS = INPUT.split(':')[4]
search_mode = 'source'

for number in re.finditer(r'(\d+)', WATER_NUMBERS):
    if search_mode == 'source':
        WATER_DATA = []  # noqa
        WATER_DATA.append(int(number.group()))
        search_mode = 'destination'
    elif search_mode == 'destination':
        WATER_DATA.append(int(number.group()))
        search_mode = 'range'
    elif search_mode == 'range':
        WATER_DATA.append(int(number.group()))
        search_mode = 'source'
        ALL_WATER_DATA.append(WATER_DATA)

print('___________water________________')
for PRINT_LIST in ALL_WATER_DATA:
    print(PRINT_LIST)

# // Verzamel light data
LIGHT_NUMBERS = INPUT.split(':')[5]
search_mode = 'source'

for number in re.finditer(r'(\d+)', LIGHT_NUMBERS):
    if search_mode == 'source':
        LIGHT_DATA = []  # noqa
        LIGHT_DATA.append(int(number.group()))
        search_mode = 'destination'
    elif search_mode == 'destination':
        LIGHT_DATA.append(int(number.group()))
        search_mode = 'range'
    elif search_mode == 'range':
        LIGHT_DATA.append(int(number.group()))
        search_mode = 'source'
        ALL_LIGHT_DATA.append(LIGHT_DATA)

print('___________light________________')
for PRINT_LIST in ALL_LIGHT_DATA:
    print(PRINT_LIST)

# // verzamel temperature data
TEMPERATURE_NUMBERS = INPUT.split(':')[6]
search_mode = 'source'

for number in re.finditer(r'(\d+)', TEMPERATURE_NUMBERS):
    if search_mode == 'source':
        TEMPERATURE_DATA = []  # noqa
        TEMPERATURE_DATA.append(int(number.group()))
        search_mode = 'destination'
    elif search_mode == 'destination':
        TEMPERATURE_DATA.append(int(number.group()))
        search_mode = 'range'
    elif search_mode == 'range':
        TEMPERATURE_DATA.append(int(number.group()))
        search_mode = 'source'
        ALL_TEMPERATURE_DATA.append(TEMPERATURE_DATA)

print('___________temperature________________')
for PRINT_LIST in ALL_TEMPERATURE_DATA:
    print(PRINT_LIST)

# // verzamel humidity data
HUMIDITY_NUMBERS = INPUT.split(':')[7]
search_mode = 'source'

for number in re.finditer(r'(\d+)', HUMIDITY_NUMBERS):
    if search_mode == 'source':
        HUMIDITY_DATA = []  # noqa
        HUMIDITY_DATA.append(int(number.group()))
        search_mode = 'destination'
    elif search_mode == 'destination':
        HUMIDITY_DATA.append(int(number.group()))
        search_mode = 'range'
    elif search_mode == 'range':
        HUMIDITY_DATA.append(int(number.group()))
        search_mode = 'source'
        ALL_HUMIDITY_DATA.append(HUMIDITY_DATA)

print('___________humidity________________')
for PRINT_LIST in ALL_HUMIDITY_DATA:
    print(PRINT_LIST)

# // verzamel location data
LOCATION_NUMBERS = INPUT.split(':')[8]
search_mode = 'source'

for number in re.finditer(r'(\d+)', LOCATION_NUMBERS):
    if search_mode == 'source':
        LOCATION_DATA = []  # noqa
        LOCATION_DATA.append(int(number.group()))
        search_mode = 'destination'
    elif search_mode == 'destination':
        LOCATION_DATA.append(int(number.group()))
        search_mode = 'range'
    elif search_mode == 'range':
        LOCATION_DATA.append(int(number.group()))
        search_mode = 'source'
        ALL_LOCATION_DATA.append(LOCATION_DATA)

print('___________location________________')
for PRINT_LIST in ALL_LOCATION_DATA:
    print(PRINT_LIST)

# _____________________ locatie zoeken ___________________-


def find_dest(old_source, lists_to_scan):
    for list_data in lists_to_scan:
        min_source_num = int(list_data[1])
        min_dest = int(list_data[0])
        dest_range = int(list_data[2])
        difference = int(old_source) - int(min_source_num)
        if difference in range(0, dest_range):
            new_source = int(min_dest) + difference
            print(f'old: {old_source} new: {new_source}')
            break
        else:
            new_source = int(old_source)
            print(f'new: {new_source}')
    return new_source


for source in SEEDS:
    for data_list in ALL_FULL_DATAS_LIST:
        source = find_dest(source, data_list)
        print(source)
    print(f'Location: {source}')
    location_list.append(source)
print(location_list)

lowest_number = None
for location in location_list:
    if lowest_number is None:
        lowest_number = location
    elif location < lowest_number:
        lowest_number = location

print(f'FINAL RESULT: {lowest_number}')




    # # // soil
    # for soil_data in ALL_SOIL_DATA:
    #     min_seed_number = int(soil_data[1])
    #     min_dest = int(soil_data[0])
    #     seed_range = int(soil_data[2])
    #     difference = int(seed_source) - int(min_seed_number)
    #     if difference in range(0, seed_range):
    #         soil_source = int(min_dest) + difference
    #         print(f'new: {soil_source}')
    #         break
    #     else:
    #         soil_source = int(seed_source)
    #         print(f'new: {soil_source}')
