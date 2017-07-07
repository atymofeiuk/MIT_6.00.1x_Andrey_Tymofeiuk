# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:33:18 2017

MIT 6.00.1x course on edX.org: PSet1 P1

Task:

Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 

@author: Andrey Tymofeiuk

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.
"""
# Andrey Tymofeiuk: Creating a list of vowels
vowels = ['a','e','i','o','u']
# Andrey Tymofeiuk: 
count = 0

# Andrey Tymofeiuk: Iterative for loop; s is given by edX grader
for el in s:
    if el in vowels:
        count += 1
        
print("Number of vowels: " + str(count))