import string

password = 'hxbxwxba'
req1 = False
req2 = False
req3 = False

alphabet = string.ascii_lowercase

while any(req is False for req in [req1, req2, req3]):
    req1 = False
    req2 = False
    req3 = False
    pairs_of_letters = 0
    pair_found = ''

    # // change_password
    new_password = ''
    z_replaced = 0
    for index, letter in enumerate(password[::-1]):
        if password[-(index + 1)] != 'z':
            current_letter_index = alphabet.index(password[-(index + 1)])
            new_password += password[:-(index + 1)]
            new_letter = alphabet[current_letter_index + 1]
            new_password += new_letter
            break
        else:
            z_replaced += 1

    new_password += z_replaced * 'a'
    password = new_password

    # // requirement 1
    for i in range(len(password) - 2):
        pair = password[i:i + 3]
        if pair in alphabet:
            req1 = True
            break

    # // requirement 2
    if 'i' not in password and 'l' not in password and 'o' not in password:
        req2 = True

    # // requirement 3
    for letter in alphabet:
        if password.count(2 * letter) != 0:
            if 2 * letter != pair_found:
                pairs_of_letters += 1
                pair_found = 2 * letter

    if pairs_of_letters >= 2:
        req3 = True

    print(password)

print(password)
