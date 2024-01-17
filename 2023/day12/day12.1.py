import functools
import pprint


INPUT = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()

print(INPUT)

springs_list_full = []

for item in INPUT:
    springs = item.split(' ')[0]
    spring_count = list(map(int, item.split(' ')[1].split(',')))
    spring_tuple = (springs, spring_count)
    springs_list_full.append(spring_tuple)

# pprint.pprint(spring_list)


@functools.cache
def calc_possibility_num(spring_string, number_of_strings_list):
    if not number_of_strings_list:
        if '#' not in spring_string:
            return 1
        else:
            return 0

    if not spring_string:
        return 0

    next_spring = spring_string[0]
    next_spring_number = number_of_strings_list[0]
    print(spring_string, number_of_strings_list)

    def hashtag():
        new_group = number_of_strings_list[:next_spring]
        new_group = new_group.replace('?', '#')


    def dot():
        return calc_possibility_num(spring_string[1:],  number_of_strings_list)

    if next_spring == '#':
        hashtag()
    elif next_spring == '.':
        dot()
    elif next_spring == '?':
        hashtag() + dot()

    print(next_spring)
    print(next_spring_number)


for strings, string_numbers in springs_list_full:
    calc_possibility_num(strings, tuple(string_numbers))

