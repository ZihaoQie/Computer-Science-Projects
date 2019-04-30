#Point Class

#class <name>:
#All class functions and data members are public in python.

import math
class Point():
    ''' x-value measures the Quantity and Y-value measures the Price (at certain particular quantity)
    counter is a class attribute '''
    counter=0
    
    #initialize function

    def __init__(self, x_coord=0, y_coord=0):
        self.x=x_coord
        self.y=y_coord
        Point.counter+=1

    def __str__ (self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    #set and get functions, setter and getter functions
    def setX(self, x_coord):
        if type(x_coord)==int:
            self.x=x_coord

    def setY(self, y_coord):
        if type(y_coord)==int:
            self.y=y_coord

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def slope(self, other):
        # The slope of supply curve/demand curve
        result= (other.y-self.y)/(other.x-self.x)
        return result

       








