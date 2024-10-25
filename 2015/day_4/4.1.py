import hashlib

code = 'iwrupvqb'
current_number = 0

while True:
    full_code = bytes(f'{code}{current_number}', 'utf-8')
    hashed_string = hashlib.md5(full_code).hexdigest()
    current_number += 1

    if hashed_string[0:6] == '00000':
        print(current_number - 1)
        break
