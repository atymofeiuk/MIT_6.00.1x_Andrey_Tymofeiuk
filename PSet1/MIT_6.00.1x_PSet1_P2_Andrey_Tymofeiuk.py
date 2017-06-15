# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:59:02 2017

MIT 6.00.1x course on edX.org: PSet1 P2

{
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
}

@author: Andrey Tymofeiuk
"""

#Andrey Tymofeiuk: s is given by edX

#Andrey Tymofeiuk: Setting a counter and using for loop
count = 0
for el in range(len(s)-2):
    if s[el] == "b":
        if s[el+1] == "o":
            if s[el+2] == "b":
                count += 1

print(count)