# -*- coding: utf-8 -*-
"""
Created on Wed May 31 21:39:40 2017

MIT 6.00.1x course on edX.org: PSet1 P3

Task: 
    
Assume s is a string of lower case characters. 
Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""
#Andrey Tymofeiuk: s is given by edX.org

#Andrey Tymofeiuk: Defining necessary variables
longest = 0
length = 0
order = 0

#Andrey Tymofeiuk: Using nested loops approach, both for and while loops
for el in range(len(s)-2):
    k = 0
    while s[el+k] <= s[el+k+1]:
        k += 1
        if el+k+1 == len(s):
            break
    if k > length:
        length = k
        order = el
#Andrey Tymofeiuk: Determining the longest loop by its index
longest = s[order:order + length+1]

print("Longest substring in alphabetical order is:" + longest)
