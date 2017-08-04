# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 00:23:41 2017

MIT 6.00.1x course on edX.org: Final (Problem 3)

Task:
   
Implement a function that meets the specifications below.
    - assumes s a string
    - returns an int that is the sum of all of the digits in s.
    - if there are no digits in s it raises a ValueError exception. 

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""
def sum_digits(s):
    total = 0
    count = 0
    for element in s:
        try:
            if type(int(element)) == int:
                total += int(element)
                count += 1
        except ValueError:
            pass
    if count == 0:
        raise ValueError
    else:
        return total
        