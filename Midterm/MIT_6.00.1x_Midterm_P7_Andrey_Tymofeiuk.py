# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:45:27 2017

MIT 6.00.1x course on edX.org: Midterm P7

Task: 

Write a function called dict_invert that takes in a dictionary with immutable values 
and returns the inverse of the dictionary. The inverse of a dictionary d is another 
dictionary whose keys are the unique dictionary values in d. The value for a key 
in the inverse dictionary is a sorted list (increasing order) of all keys in d 
    that have the same value in d.

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    new_dict = {}
    
    for key in d:
        if d[key] not in new_dict:  
            new_dict[d[key]] = [key]
        elif d[key] in new_dict:
            new_dict[d[key]].append(key)
   
    # Andrey Tymofeiuk: For one particular case - I don't know why they require it
    # to be sorted
    for key in new_dict:
        new_dict[key].sort()

    return new_dict
        