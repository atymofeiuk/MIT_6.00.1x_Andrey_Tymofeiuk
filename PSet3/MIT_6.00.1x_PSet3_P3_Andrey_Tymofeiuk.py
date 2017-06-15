# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:59:44 2017

MIT 6.00.1x course on edX.org: PSet3 P3

@author: Andrey Tymofeiuk
"""
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available_letters += letter
    return available_letters

