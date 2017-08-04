# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 22:14:31 2017

MIT 6.00.1x course on edX.org: Final (Problem 7)

Task: Classes Location and Campus are given. Write MITCampus class that meets the docstring specifications.

Important: This code is placed at GitHub to track my progress in programming and
to show my way of thinking. Also I will be happy if somebody will find my solution
interesting. But I respect The Honor Code and I ask you to respect it also - please
don't use this solution to pass the MIT 6.00.1x course.

@author: Andrey Tymofeiuk

"""


class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
    
class MITCampus(Campus):
    tent_collect = []
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        # Andrey Tymofeiuk: This method is written by me
        self.center_loc = center_loc
        self.tent_loc = tent_loc
        MITCampus.tent_collect = []
        MITCampus.tent_collect.append(tent_loc)
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        # Andrey Tymofeiuk: This method is written by me
        if new_tent_loc in MITCampus.tent_collect:
            return False
        for tent in MITCampus.tent_collect:
            if tent.dist_from(new_tent_loc) < 0.5:
                return False
        MITCampus.tent_collect.append(new_tent_loc)
        return True

        
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        # Andrey Tymofeiuk: This method is written by me
        try:
            MITCampus.tent_collect.remove(tent_loc)
        except:
            raise ValueError
        
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        # Andrey Tymofeiuk: This method is written by me
        tents_list = []
        coord_x = []
        coord_y = []
        for tent in MITCampus.tent_collect:
            tents_list.append(tent.__str__())
            coord_x.append(tent.getX())
            coord_y.append(tent.getY())
        check = 0
        for index1 in range(len(coord_x)):
            for index2 in range(len(coord_x)):
                if coord_x[index1] == coord_x[index2] and coord_y[index1] != coord_y[index2]:
                    check += 1
        if check != 0:
            dict = {}
            for index in range(len(tents_list)):
                if coord_x[index] not in dict.keys():
                    dict[coord_x[index]] = [tents_list[index]]
                else:
                    dict[coord_x[index]].append(tents_list[index])
            sorted_coord_x = sorted(coord_x)
            final_list = []
            for index in range(len(sorted_coord_x)):
                if len(dict.get(sorted_coord_x[index])) == 1:
                    final_list.append(dict.get(sorted_coord_x[index])[0])
                else:
                    if dict.get(sorted_coord_x[index]) not in final_list:
                        for element in dict.get(sorted_coord_x[index]):
                            final_list.append(element)                    
            final_final_list = []
            for element in final_list:
                if element not in final_final_list:
                    final_final_list.append(element)
            return final_final_list
        else:
            tents_list = []
            coordinates = []
            for tent in MITCampus.tent_collect:
                tents_list.append(tent.__str__())
                coordinates.append(tent.getX())
            dict = {}
            for index in range(len(tents_list)):
                dict[coordinates[index]] = tents_list[index]
            sorted_coordinates = sorted(coordinates)
            final_list = []
            for index in range(len(sorted_coordinates)):
                final_list.append(dict.get(sorted_coordinates[index]))
            return final_list
    
    
#c = MITCampus(Location(1,2))
#print(c.add_tent(Location(1,2)))
#print(c.add_tent(Location(0,0)))
#print(c.add_tent(Location(2,3)))
#print(c.add_tent(Location(2,3)))
#print(c.get_tents())
#
#c = MITCampus(Location(1,2))
#print(c.add_tent(Location(2,3)))
#print(c.add_tent(Location(1,2)))
#print(c.add_tent(Location(0,0)))
#print(c.add_tent(Location(2,3)))
#print(c.get_tents())
#        
#c = MITCampus(Location(-1,-2))
#print(sorted(c.get_tents()))

#c = MITCampus(Location(1,2),Location(-1,-2))
#print(c.add_tent(Location(1,2))) # this should actually work!
#print(c.add_tent(Location(-1,-2)))
#print(c.add_tent(Location(-1,-2)))
#print(c.add_tent(Location(-1,-2)))
#print(c.add_tent(Location(-1,-2)))
#print(sorted(c.get_tents()))
#
#c = MITCampus(Location(-1,-2))
#print(sorted(c.get_tents()))

#c = MITCampus(Location(1,2), Location(0,0))
#c.add_tent(Location(10,10))
#print(c.add_tent(Location(10,10)))

#c = MITCampus(Location(1,2), Location(0,0))
#print(c.add_tent(Location(1,2)))

#c = MITCampus(Location(1,2), Location(0,0))
#c.add_tent(Location(1,1))
#try:
#    c.remove_tent(Location(1,1))
#except ValueError:
#    print("ValueError received.")
#else:
#    print("Done!")

#c = MITCampus(Location(1,2))
#try:
#    c.remove_tent(Location(0,0))
#except ValueError:
#    print("ValueError received.")
#else:
#    print("Done!")

#c = MITCampus(Location(1,2), Location(10,10))
#try:
#    c.remove_tent(Location(10,10))
#except ValueError:
#    print("ValueError received.")
#else:
#    print("Done!")

#c = MITCampus(Location(1,2),Location(10,20))
#print(sorted(c.get_tents()))

#c = MITCampus(Location(1,2), Location(0,0))
#print(c.add_tent(Location(1,2)))

    #c = MITCampus(Location(1,2),Location(10,20))
    #print(sorted(c.get_tents()))

#c = MITCampus(Location(1,2), Location(0,1))
#print(c.add_tent(Location(1,2)))
#print(c.add_tent(Location(2,3)))
#print(c.add_tent(Location(-1,-2)))
#print(c.add_tent(Location(-2,-3)))
#print(sorted(c.get_tents()))

#c = MITCampus(Location(1,2),Location(-1,-2))
#print(c.add_tent(Location(1,2))) # this should actually work!
#print(c.add_tent(Location(-1,-2)))
#print(c.add_tent(Location(-1,-2)))
#print(c.add_tent(Location(-1,-2)))
#print(c.add_tent(Location(-1,-2)))
#print(sorted(c.get_tents()))

#check if add_tent allows adding a tent closer than 0.5
#c = MITCampus(Location(1,2), Location(3,1))
#print(c.add_tent(Location(2.5,1)))
#c = MITCampus(Location(1,2), Location(3,1))
#print(c.add_tent(Location(2.49,1)))
#c = MITCampus(Location(1,2), Location(3,1))
#print(c.add_tent(Location(2.51,1)))

#c = MITCampus(Location(1,2), Location(0,1))
#c.add_tent(Location(-1,2))
#c.add_tent(Location(1,-10))
#c.add_tent(Location(1,10))
#c.add_tent(Location(1,20))
#c.add_tent(Location(1,40))
#print(sorted(c.get_tents()))

#check if add_tent allows adding a tent closer than 0.5
#c = MITCampus(Location(1,2), Location(3,1))
#print(c.add_tent(Location(2.5,1)))
#c = MITCampus(Location(1,2), Location(3,1))
#print(c.add_tent(Location(2.49,1)))
#c = MITCampus(Location(1,2), Location(3,1))
#print(c.add_tent(Location(2.51,1)))
#
#check if add_tent allows adding a tent closer than 0.5
#again, but what disallows placement is the SECOND tent this time
#c = MITCampus(Location(1,2), Location(3,1))
#c.add_tent(Location(1,1))
#print(c.add_tent(Location(1.5,1)))
#c = MITCampus(Location(1,2), Location(3,1))
#c.add_tent(Location(1,1))
#print(c.add_tent(Location(1.49,1)))
#c = MITCampus(Location(1,2), Location(3,1))
#c.add_tent(Location(1,1))
#print(c.add_tent(Location(1.51,1)))
#
##two equidistant tents from desired new tent_loc
#c = MITCampus(Location(1,2), Location(1,0))
#c.add_tent(Location(0,1))
#print(c.add_tent(Location(0,0)))