# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:57:00 2017

MIT 6.00.1x course on edX.org: PSet3 P1

Task: 
    
Please read the Hangman Introduction before starting this problem. We'll start
by writing 3 simple functions that will help us easily code the Hangman 
problem. First, implement the function isWordGuessed that takes in two 
parameters - a string, secretWord, and a list of letters, lettersGuessed. 
This function returns a boolean - True if secretWord has been guessed (ie, 
all the letters of secretWord are in lettersGuessed) and False otherwise.

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
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
