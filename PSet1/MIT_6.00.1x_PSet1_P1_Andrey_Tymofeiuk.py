# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:33:18 2017

MIT 6.00.1x course on edX.org: PSet1 P1

{
Assume s is a string of lower case characters. Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
}

@author: Andrey Tymofeiuk
"""
# Andrey Tymofeiuk: Creating a list of vowels
vowels = ['a','e','i','o','u']

count = 0

# Andrey Tymofeiuk: Iterative for loop; s is given
for el in s:
    if el in vowels:
        count += 1
        
print("Number of vowels: " + str(count))