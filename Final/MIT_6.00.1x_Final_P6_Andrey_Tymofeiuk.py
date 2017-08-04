# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 08:03:47 2017

MIT 6.00.1x course on edX.org: Final (Problem 6)

Task: Class Container is given. Write the subclasses subject to docstring.

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.

@author: Andrey Tymofeiuk

"""

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # Andrey Tymofeiuk: This method is written by me
        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # Andrey Tymofeiuk: This method is written by me
        if self.vals.get(e) == None:
            return 0
        return self.vals.get(e)
    
    def __add__(self, other):
        # Andrey Tymofeiuk: This method is written by me
        copy_self = self.vals.copy()
        copy_other = other.vals.copy()
        keys_self = self.vals.keys()
        keys_other = other.vals.keys()
        new_dict = Container()
        for key in keys_self:
            for limit in range(copy_self.get(key)):
                new_dict.insert(key)
        for key in keys_other:
            for limit in range(copy_other.get(key)):
                new_dict.insert(key)
        return Bag.__str__(new_dict)

class ASet(Container):
    count = {}
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # Andrey Tymofeiuk: This method is written by me
        if e in self.vals:
            self.vals[e] = 0
            ASet.count[e] = 1

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # Andrey Tymofeiuk: This method is written by me
        if e in self.vals and ASet.count.get(e) == None:
            return True
        else:
            return False
