# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 18:17:58 2017

MIT 6.00.1x course on edX.org: Midterm P4

Task:

Write a function is_triangular that meets the specification below. 
A triangular number is a number obtained by the continued summation of 
integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., 
corresponding to 1, 3, 6, 10, etc., are triangular numbers.

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    #Andrey Tymofeiuk: Declare variable and list for collection
    summary = 0
    collection = []
    
    # Andrey Tymofeiuk: Corner case
    if k == 1:
        return True
    
    for element in range(k):
        summary += element
        collection.append(summary)
        
    if k in collection:
        return True
    else:
        return False
