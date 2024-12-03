import re
numbers = re.findall(r'-?\d+', open('main.txt').read())
numbers = list(map(int, numbers))
print(sum(numbers))
