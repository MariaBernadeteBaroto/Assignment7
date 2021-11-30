# ask for a sentence input

text = input('Enter a sentence: ')
char1 = ' '
char2 = 'aeiouAEIOU'


# display the number of words

def count_char(char1, text):
    count = 0
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

print(f'number of words are {words}')
print(f'the number of vowels are {vowels}:')


# display the number of consonants
