strings = open('sample.txt').readlines()
total_length = sum(len(x) for x in strings)
string_values = 0

for string in strings:
    string = string.strip()
    