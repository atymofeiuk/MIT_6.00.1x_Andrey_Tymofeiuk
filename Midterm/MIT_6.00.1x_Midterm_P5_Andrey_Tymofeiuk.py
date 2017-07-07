# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:10:09 2017

MIT 6.00.1x course on edX.org: Midterm P5

Task:
    
Write a Python function that takes in a string and prints out a version of this string
that does not contain any vowels, according to the specification below. 
Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'. For example, if 
s = "This is great!" then print_without_vowels will print Ths s grt!

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.

"""


def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Andrey Tymofeiuk: s is given by edX grader
    new_string = ''
    old_string = s.lower()
    
    for index in range(len(s)):
        if old_string[index] != 'a' and old_string[index] != 'e' and old_string[index] != 'i' and old_string[index] != 'u' and old_string[index] != 'o':
            new_string += s[index]
    print(new_string)