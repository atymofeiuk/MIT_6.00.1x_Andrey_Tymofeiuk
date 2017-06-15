# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:57:00 2017

MIT 6.00.1x course on edX.org: PSet3 P1

@author: Andrey Tymofeiuk
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count = 0
    for el in secretWord:
        if el in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False
