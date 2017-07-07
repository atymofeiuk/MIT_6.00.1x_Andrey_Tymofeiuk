# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:58:31 2017

MIT 6.00.1x course on edX.org: PSet3 P2

Next, implement the function getGuessedWord that takes in two parameters 
- a string, secretWord, and a list of letters, lettersGuessed. This function 
returns a string that is comprised of letters and underscores, based on what 
letters in lettersGuessed are in secretWord. This shouldn't be too different 
from isWordGuessed!

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
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
