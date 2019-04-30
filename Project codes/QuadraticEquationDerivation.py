# Deriving quadratic function from 3 known points

def GetQuadraticEquation(x1, y1, x2, y2, x3, y3):
    denom = (x1-x2) * (x1-x3) * (x2-x3);
    A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom;
    B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom;
    C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom;

    return A,B,C


'''
x1,y1=[Quantity1_ATC_pc, Price1_ATC_pc]
x2,y2=[Quantity2_ATC_pc, Price2_ATC_pc]
x3,y3=[Quantity3_ATC_pc, Price3_ATC_pc]
'''

#For a pc firm.


Q1_ATC_pc=int(input(Please enter the quantity value of the first data point on the Average Total Cost.))
P1_ATC_pc=int(input(Please enter the price value of the first data point on the Average Total Cost.))

Q2_ATC_pc=int(input(Please enter the quantity value of the 2nd data point on the Average Total Cost.))
P2_ATC_pc=int(input(Please enter the price value of the 2nd data point on the Average Total Cost.))

Q3_ATC_pc=int(input(Please enter the quantity value of the 3rd data point on the Average Total Cost.))
P3_ATC_pc=int(input(Please enter the price value of the 3rd data point on the Average Total Cost.))





a,b,c=GetQuadraticEquation(x1, y1, x2, y2, x3, y3)

