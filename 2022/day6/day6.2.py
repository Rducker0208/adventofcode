datastream = open('main.txt').read()
first_characters = datastream[0:14]

if all(first_characters.count(char) == 1 for char in first_characters):
    print(4)


for i in range(14, len(datastream)):
    string_to_check = datastream[i - 14: i]
    if all(string_to_check.count(char) == 1 for char in string_to_check):
        print(i)
        quit()
