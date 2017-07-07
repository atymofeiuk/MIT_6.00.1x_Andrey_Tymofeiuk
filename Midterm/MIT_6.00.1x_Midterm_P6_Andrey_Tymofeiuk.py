# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:29:52 2017

MIT 6.00.1x course on edX.org: Midterm P6

Task: 
    
Write a function that satisfies the docstring

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""

def largest_odd_times(L):
    
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    # Andrey Tymofeiuk: Sometimes double mistake leads to peculiar right result
    dict_collect = {}
    list_final = []
    
    for element in L:
        if element in dict_collect:
            dict_collect[element] += 1
        else:
            dict_collect[element] = 0
    
    for key in dict_collect:
        if dict_collect[key] % 2 == 0:
            list_final.append(key)
    
    if list_final != []:
        return max(list_final)
    else:
        return None


    
    