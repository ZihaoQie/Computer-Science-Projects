# Class Line

import math
from Point import Point

class Line():
    
    def __init__(self, P1, P2):
        self.P1=P1
        self.P2=P2
        self.slope=(P2.y-P1.y)/(P2.x-P1.x)
        self.intercept=P1.y-(self.slope)*P1.x

    def __str__(self):
        return '(P1::' + str(self.P1) + "P2: " + str(self.P2) + ')'



