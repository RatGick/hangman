from random import randint

# ===========SETTINGS=============
# Firstly create a list of guessing word
words = ('charcoal', 'panda', 'hyperventilation', 'violence')
# Secondly, number of wrongly guessed letters
tries_number = 5


# ===========FUNCTIONS============


def find_ch(letter, word):
    indexes = []
    word = list(word)
    for i in range(len(word)):
        if word[i] == letter:
            indexes.append(i)
    return indexes


def letter_check(letter, word):
    global tries_number
    if word.count(letter) == 0:
        tries_number -= 1
        print(f'{letter} is seems to not be included, boy.\n')
        print(f'You have {tries_number} attempts left.\n')
        return False
    else:
        print('You are right!')
        return True


# ===========BODY=================

# Firstly grab one random word from the list
word = words[randint(0, len(words) - 1)]
# Display a greeting, masked word and ask a user to enter a letter
word_masked = '*' * len(word)
print(
    f'Hello! We are glad to introduce you the hangman game!\nYour word is {word_masked}.\nYou have {tries_number} attempts left\n')
# Looping script stuff while there are tries and word is not guessed
while tries_number > 0 and word_masked.count('*') != 0:
    # Waiting for the entered letter and checking if it's actually a single letter
    letter = str(input('Please, enter your letter: '))
    while len(letter) > 1:
        letter = str(input('Please, enter a SINGLE letter: '))
    # Check the letter
    if letter_check(letter, word):
        indexes = find_ch(letter, word)
        word_masked = list(word_masked)
        for i in range(len(indexes)):
            word_masked[indexes[i]] = letter
        word_masked = ''.join(word_masked)
        print(word_masked)
    # Check number of attempts
    if tries_number < 1:
        print('Sorry, but the game is over')
