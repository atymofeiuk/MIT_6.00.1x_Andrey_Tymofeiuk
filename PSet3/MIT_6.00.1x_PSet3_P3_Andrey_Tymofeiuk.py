# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:59:44 2017

MIT 6.00.1x course on edX.org: PSet3 P3

Task:
    
Next, implement the function getAvailableLetters that takes in one parameter - 
a list of letters, lettersGuessed. This function returns a string that is 
comprised of lowercase English letters - all lowercase English letters that 
are not in lettersGuessed.

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available_letters = ""
    for letter in string.ascii_lowercase: # Andrey Tymofeiuk: string was imported
        if letter not in lettersGuessed:
            available_letters += letter
    return available_letters

