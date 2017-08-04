# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 07:15:08 2017

MIT 6.00.1x course on edX.org: Final (Problem 5)

Task: Implement a function cipher according to docstring documentation

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.

@author: Andrey Tymofeiuk

"""

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    dict = {}
    for index in range(len(map_from)):
        dict[map_from[index]] = map_to[index]
    decoded = ''
    for index in range(len(code)):
        decoded += dict.get(code[index])
    return (dict, decoded)
