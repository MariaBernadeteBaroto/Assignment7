# ask for a sentence input

text = input('Enter a sentence: ')
char = ' '


# display the number of words

def count_char(char, text):
    count = 0
    for c in text:
        for d in char:
            if c == d:
                count = count+1
    return count

words = count_char(char, text)

print(words)


# display the number of vowels

# display the number of consonants
