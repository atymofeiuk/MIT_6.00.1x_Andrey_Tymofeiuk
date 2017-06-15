# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 14:00:34 2017

MIT 6.00.1x course on edX.org: PSet3 P4

@author: Andrey Tymofeiuk
"""
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("-------------")
    
    tries = 8
    lettersGuessed = []
    
    while True:
        print("You have " + str(tries) + " guesses left")
        print("Available Letters: ", end ="")
        print(getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            print("-------------")
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(guess)
            tries -= 1
            print("-------------")
        
        if tries == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            break
        elif isWordGuessed(secretWord, lettersGuessed) == True:
            print("Congratulations, you won!")
            break
