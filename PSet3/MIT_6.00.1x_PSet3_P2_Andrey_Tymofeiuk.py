# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:58:31 2017

MIT 6.00.1x course on edX.org: PSet3 P2

@author: Andrey Tymofeiuk
"""
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guess = ""
    for letter in secretWord:
        if letter in lettersGuessed:
            guess += letter
        else:
            guess += " _"
    return guess
