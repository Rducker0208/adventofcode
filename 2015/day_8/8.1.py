lines = open('main.txt').readlines()
total_string_lengths = 0
string_values = 0
strings = []

for string in lines:
    string = string.strip()
    string = string[1:-1]
    total_string_lengths += len(string)

    string = string.replace(r"\\", "\\")
    string = string.replace(r'\"', '"')

    for i in range(len(string) - 3):
        characters = string[i:i+4]

        if characters[:2] == r'\x':
            try:
                decimal_value = int(characters[2:], 16)
                ascii_string = chr(decimal_value)

                string = string.replace(characters, ascii_string)

            except ValueError:
                pass

    strings.append(string)

    string_values += (len(string) - 2)

print(total_string_lengths - string_values)
print(total_string_lengths)