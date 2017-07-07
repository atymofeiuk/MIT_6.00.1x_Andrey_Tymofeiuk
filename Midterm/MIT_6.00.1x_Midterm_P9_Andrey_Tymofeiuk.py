# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 19:25:12 2017

MIT 6.00.1x course on edX.org: Midterm P8

Task:

Write a Python function that takes in two lists and calculates whether they are 
permutations of each other. The lists can contain both integers and strings. We 
define a permutation as follows:

the lists have the same number of elements
list elements appear the same number of times in both lists

If the lists are not permutations of each other, the function returns False. 
If they are permutations of each other, the function returns a tuple consisting
of the following elements:

the element occuring the most times
how many times that element occurs
the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None). If more than one 
element occurs the most number of times, you can return any of them.

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Andrey Tymofeiuk: Corner case
    if L1 == [] and L2 == []:
        return (None, None, None)
    
    # Andrey Tymofeiuk: Two dicts for collection
    dict_L1 = {}
    dict_L2 = {}
    final_tuple = ()
    
    # Andrey Tymofeiuk: 1st dict collection
    for index in range(len(L1)):
        if L1[index] not in dict_L1:
            dict_L1[L1[index]] = 1
        elif L1[index] in dict_L1:
            dict_L1[L1[index]] += 1
    # Andrey Tymofeiuk: 2nd dict collection
    for index in range(len(L2)):
        if L2[index] not in dict_L2:
            dict_L2[L2[index]] = 1
        elif L2[index] in dict_L2:
            dict_L2[L2[index]] += 1
            
    # Andrey Tymofeiuk: Get final tuple if they are equal
    if dict_L1 == dict_L2:
        longest = 0
        for key in dict_L1:
            if dict_L1[key] > longest:
                longest = dict_L1[key]
                remember_the_key = key
        final_tuple = (remember_the_key,) + (longest,) + (type(remember_the_key),)
        return final_tuple
    else:
        return False
            
            
        
    
    
    
    
    