# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 22:32:47 2017

MIT 6.00.1x course on edX.org: Final (Problem 4)

Task: Implement a function that meets the specifications below:
    
        t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.

@author: Andrey Tymofeiuk

"""
def helper(t):
    if type(t) == list or type(t) == tuple:
        if len(t) == 0:
            return []
        return helper(t[0]) + helper(t[1:])   
    return [t]

def max_val(t):
    return max(helper(t))
