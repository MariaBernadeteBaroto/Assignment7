# Program 2: Password validator
# ask for a input password

password = input('Enter your password: ')
char1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
# have at least one special character