# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 19:07:14 2017

MIT 6.00.1x course on edX.org: Midterm P8

Task:

Write a function called general_poly, that meets the specifications below. 

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""
def general_poly(L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def helper(x):
        summary = 0
        turnout = len(L)-1
        for index in range(len(L)):
            summary += L[index]*(x**turnout)
            turnout -= 1
        return summary
    
    return helper

print(general_poly([1, 2, 3, 4])(10))
