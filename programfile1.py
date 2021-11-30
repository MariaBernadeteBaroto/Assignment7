# ask for a sentence input

text = input('Enter a sentence: ')
char1 = ' '
char2 = 'aeiouAEIOU'
char3 = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'


# display the number of words

def count_char(char1, text):
    count = 1
    for c in text:
        for d in char1:
            if c == d:
                count = count+1
    return count

words = count_char(char1, text)

# display the number of vowels

def count_char(char2, text):
    count = 0
    for c in text:
        for d in char2:
            if c == d:
                count = count+1
    return count

vowels = count_char(char2, text)


# display the number of consonants

def count_char(char3, text):
    count = 0
    for c in text:
        for d in char3:
            if c == d:
                count = count+1
    return count

consonants = count_char(char3, text)


print(f'number of words: {words}')
print(f'number of vowels: {vowels}:')
print(f'number of consonants: {consonants}')


