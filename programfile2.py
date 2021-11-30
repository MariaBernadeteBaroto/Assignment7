# Program 2: Password validator
# ask for a input password

password = input('Enter your password: ')
char1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
char2 = '0123456789'
char3 = '!@#$%^&*()_+{}:"|<>?[]\;/.,=-+'

# check if the password is valid
# check if the password is greater than 15 letters

if len(password) <= 15:
    print('password not valid!')

# have at least one capital letter
def count_char(char1, password):
    count = 0
    for c in password:
        for d in char1:
            if c == d:
                count = count+1
    return count
capital = count_char(char1, password)

if capital == 0:
    print('password not valid!')

# have at least one number
def count_char(char2, password):
    count = 0
    for c in password:
        for d in char2:
            if c == d:
                count = count+1
    return count
number = count_char(char2, password)

if number == 0:
    print('password not valid!')

# have at least one special character
def count_char(char3, password):
    count = 0
    for c in password:
        for d in char3:
            if c == d:
                count = count+1
    return count
special = count_char(char3, password)

if special == 0:
    print('password not valid!')

# check if all conditions were satisfied then password is valid
if len(password) > 15:
    if capital > 0:
        if number > 0:
            if special > 0:
                print('VALID PASSWORD!')


