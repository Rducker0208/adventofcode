import aoc_lube
RACES = aoc_lube.fetch(year=2023, day=6).splitlines()
# RACES = """Time:      7  15   30
#            Distance:  9  40  200""".splitlines()
TIMES_FULL = RACES[0].split(':')[1]
DISTANCES_FULL = RACES[1].split(':')[1]

TIMES = []
DISTANCES = []
possible_ways_list = []

possible_ways_total = 0

for item in TIMES_FULL.split(' '):
    if item != '':
        TIMES.append(int(item))

for item in DISTANCES_FULL.split(' '):
    if item != '':
        DISTANCES.append(int(item))

print(RACES)
print(TIMES)
print(DISTANCES)


def get_min_or_max(time_list, mode, race_distance, race_time):
    for time_hold in range(0, race_time + 1):
        time_left = race_time - time_hold
        meter_per_ms = time_hold

        distance_made = time_left * meter_per_ms

        if distance_made > race_distance:
            print('___________________________')
            print(f'Made it to finish line!\n'
                  f'Race: {race_time}\n'
                  f'Time hold: {time_hold}')
            print('___________________________')
            number_possible = time_hold
            if mode == 'min_num':
                return number_possible
    return number_possible


for race_number, race in enumerate(TIMES):
    minimum_number = get_min_or_max(TIMES, 'min_num', DISTANCES[race_number], race)
    max_number = get_min_or_max(TIMES, 'max_num', DISTANCES[race_number], race)

    print(f'Race number: {race}\n'
          f'Min number: {minimum_number}\n'
          f'Max number: {max_number}\n')

    possible_ways = max_number - minimum_number + 1
    if possible_ways_total == 0:
        possible_ways_total += possible_ways
    else:
        possible_ways_total *= possible_ways

print(possible_ways_total)