# Program 2: Password validator
# ask for a input password

password = input('Enter your password: ')

# check if the password is valid
# check if the password is greater than 15 letters

if len(password) <= 15:
    print('password not valid!')
    
# have at least one capital letter
# have at least one number
# have at least one special character