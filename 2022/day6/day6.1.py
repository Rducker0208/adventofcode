datastream = open('main.txt').read()
first_characters = datastream[0:4]

if all(first_characters.count(char) == 1 for char in first_characters):
    print(4)


for i in range(4, len(datastream)):
    string_to_check = datastream[i - 4: i]
    if all(string_to_check.count(char) == 1 for char in string_to_check):
        print(i)
        quit()
