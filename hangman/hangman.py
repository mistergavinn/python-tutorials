import random
from words import words
import string

def getValidWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    word = getValidWord(words)
    wordLetters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set() # what the user has guessed

    # getting user input
    while len(wordLetters) > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd
        print('You have used these letters: ', ' '.join(usedLetters))

        # what the current word is (ie W - R D)
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current word: ', ' '.join(wordList))

        userLetter = input('Guess a letter: ').upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)

        elif userLetter in usedLetters:
            print('You have already guessed that character! Please try again.')

        else:
            print('Invalid character. Please try again.')
        

hangman()