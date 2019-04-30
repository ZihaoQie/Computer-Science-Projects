# Main frame of the project
# CSCI1101 Project-Barry Qie


import math
from Point import Point
from Line import Line
import matplotlib.pyplot as plt
import numpy as np

def GetIntersection_monopoly(Line_MC_monopoly, Line_D_monopoly):
    
    for i in range (0, 70):
        temp_MR_monopoly= 2*Line_D_monopoly.slope * i + Line_D_monopoly.intercept
        temp_MC_monopoly= Line_MC_monopoly.slope* i + Line_MC_monopoly.intercept
        print("Producing at ",i,":", "Marginal Revenue:", temp_MR_monopoly, "Marginal Cost:", temp_MC_monopoly)
        
        if (int(temp_MR_monopoly)==int(temp_MC_monopoly)):
            #approximated values since we chopped out the decimals
            global equilibrium_Q
            equilibrium_Q=i
            return equilibrium_Q
            break
        
def GetIntersection_PC(Line_MR_pc, Line_MC_pc):
    
    for i in range (0, 70):
        temp_MR_pc= Price_pc
        temp_MC_pc= Line_MC_pc.slope* i
        temp_MC_pc+= Line_MC_pc.intercept
        
        print (Line_MC_pc.intercept)
        print("Producing at ",i,":", "Marginal Revenue (Demand):", temp_MR_pc, "Marginal Cost:", temp_MC_pc)
        
        if (int(temp_MR_pc)==int(temp_MC_pc)):
            #approximated values since we chopped out the decimals
            global equilibrium_Q
            equilibrium_Q=i
            return equilibrium_Q
            break
        

def GetQuadraticEquation(x1, y1, x2, y2, x3, y3):
    denom = (x1-x2) * (x1-x3) * (x2-x3);
    A     = (x3 * (y2-y1) + x2 * (y1-y3) + x1 * (y3-y2)) / denom;
    B     = (x3*x3 * (y1-y2) + x2*x2 * (y3-y1) + x1*x1 * (y2-y3)) / denom;
    C     = (x2 * x3 * (x2-x3) * y1+x3 * x1 * (x3-x1) * y2+x1 * x2 * (x1-x2) * y3) / denom;

    return A,B,C



# __main__

print ("Welcome to the Firm profits & loss calculator. Press enter to continue.")
print ("For more information about the Economic theories behind the different types of firm, please read https://courses.lumenlearning.com/boundless-economics/chapter/perfect-competition/")
print ("The following key assumptions are made: 1. Marginal Cost exhibits a linear growth along increasing quantity of output. Average Total Cost exhibits a parabolic shape due to the 3 phases of return to scale")
print ("The notion of 'price' in this calculator program refers broadly to all appropriate parameters with unit of dollar sign/ monetary parameter. ")

m=int(input("Please enter the type of your firm: 1. Perfectly Competitive Firm. 2. Monopoly."))


# The firm is a p.c. firm
if (m==1):
      #Deriving the horizontal demand curve with 2 points of same y-value (price) provided by users
      Price_pc= int(input("Please enter the market price of your homogenous product: "))
      print ("The demand and marginal revenue of your product is", Price_pc, "$/unit of output: ")

      
      P1_pc=int(input ("Please enter the price of the first sales data for demand: "))
      Q1_pc=int(input('Please enter the quantity of the first sales data: '))
      point1_demand_pc=Point(Q1_pc,P1_pc)
      print("Point 1 on the perfectly competitive firm's demand curve:", point1_demand_pc)
      
      P2_pc=int(input ("Please enter the price of the second sales data for demand: "))
      Q2_pc=int(input("Please enter the quantity of the second sales data for demand: "))
      point2_demand_pc=Point(Q2_pc,P2_pc)
      print ("Point 2 on the perfectly competitive firm's demand curve:", point2_demand_pc)
            

      #Deriving the Marginal Cost curve for perfectly competitive firm with points provided by users
      P3_pc=int(input ("Please enter the price of the first sales data for Marginal Cost: "))
      Q3_pc=int(input('Please enter the quantity of the first sales data for Marginal Cost: '))
      point1_MC_pc=Point(Q3_pc,P3_pc)
      print("Point 1 on the Perfectly Competitive firm's Marginal Cost curve:", point1_MC_pc)
      
      P4_pc=int(input ("Please enter the price of the second sales data for Marginal Cost: "))
      Q4_pc=int(input("Please enter the quantity of the fourth sales data for Marginal Cost: "))
      point2_MC_pc=Point(Q4_pc,P4_pc)
      print ("Point 2 on the Perfectly Competitive firm's Marginal Cost curve:", point2_MC_pc)

      #Deriving the Average Total Cost curve for perfectly competitive firm with points provided by users

      Q1_ATC_pc=int(input("Please enter the quantity value of the first data point on the Average Total Cost."))
      P1_ATC_pc=int(input("Please enter the price value of the first data point on the Average Total Cost."))

      Q2_ATC_pc=int(input("Please enter the quantity value of the 2nd data point on the Average Total Cost."))
      P2_ATC_pc=int(input("Please enter the price value of the 2nd data point on the Average Total Cost."))

      Q3_ATC_pc=int(input("Please enter the quantity value of the 3rd data point on the Average Total Cost."))
      P3_ATC_pc=int(input("Please enter the price value of the 3rd data point on the Average Total Cost."))



      #Instantiation & Invoking function of the perfectly competitive firm
      Line_MR_pc=Line(point1_demand_pc, point2_demand_pc)   
      print ("The Demand & Marginal Revenue curve for the perfectly competitive firm is  P=", Line_MR_pc.slope, "q+",Line_MR_pc.intercept)
      
      Line_MC_pc=Line(point1_MC_pc, point2_MC_pc)  
      print ("The Marginal Cost curve for the perfectly competitive firm is  P=", Line_MC_pc.slope, "q+ ","(",Line_MC_pc.intercept,")")

      print("The equilibrium quantity is approximately: ", GetIntersection_PC(Line_MR_pc, Line_MC_pc), " units")

      
      a_pc,b_pc,c_pc=GetQuadraticEquation(Q1_ATC_pc,P1_ATC_pc, Q2_ATC_pc, P2_ATC_pc, Q3_ATC_pc, P3_ATC_pc)
      print("The equation for Average Total Cost is: ",a_pc, 'q^2 +',b_pc,'q +', c_pc,'= P')


      #Calculating Profit/Loss
      ATC_Qe_pc= a_pc* equilibrium_Q**2+ b_pc * equilibrium_Q + c_pc
      EquilibriumPrice_Qe=Line_MR_pc.slope * equilibrium_Q+ Line_MR_pc.intercept

      Profit= (EquilibriumPrice_Qe - ATC_Qe_pc)* equilibrium_Q
      if Profit>0:
          print ("Your firm is making ", Profit, "$ of Economic Profit")
      elif Profit<0:
          print ("Your firm is incuring ", Profit, "$ of Economic Loss")


      #Graphing the curves

      n = 80
      x= np.arange(0, n)
    
      # Demand, Marginal revenue curve of the pc firm
      y1= Line_MR_pc.slope * x + Line_MR_pc.intercept

      # MC curve of the pc firm
      y2= Line_MC_pc.slope * x + Line_MC_pc.intercept

      #ATC curve of the pc firm
      y3= a_pc *x **2 + b_pc *x + c_pc


      plt.plot(x,y1)
      plt.plot(x,y2)
      plt.plot(x,y3)
      plt.show()





# The firm is a monopoly
elif (m==2):
      # Deriving the linear demand curve for the Monopolist with points provided by users
      P1_monopoly=int(input ("Please enter the price of the first sales data for demand: "))
      Q1_monopoly=int(input('Please enter the quantity of the first sales data: '))
      point1_demand_monopoly=Point(Q1_monopoly, P1_monopoly)
      print("Point 1 on the Monopoly's demand curve:", point1_demand_monopoly)
      
      P2_monopoly=int(input ("Please enter the price of the second sales data for demand: "))
      Q2_monopoly=int(input("Please enter the quantity of the second sales data: "))
      point2_demand_monopoly=Point(Q2_monopoly, P2_monopoly)
      print ("Point 2 on the Monopoly's demand curve:", point2_demand_monopoly)

      # Deriving the linear Marginal Cost curve for the Monopolist with points provided by users
      P3_monopoly=int(input ("Please enter the price of the first sales data for Marginal Cost: "))
      Q3_monopoly=int(input('Please enter the quantity of the first sales data for Marginal Cost: '))
      point1_MC_monopoly=Point(Q3_monopoly, P3_monopoly)
      print("Point 1 on the Monopolist's Marginal Cost curve:", point1_MC_monopoly)
      
      P4_monopoly=int(input ("Please enter the price of the second sales data for Marginal Cost: "))
      Q4_monopoly=int(input("Please enter the quantity of the fourth sales data for Marginal Cost: "))
      point2_MC_monopoly=Point(Q4_monopoly,P4_monopoly)
      print ("Point 2 on the Monopolist's Marginal Cost curve:", point2_MC_monopoly)

      # Deriving the Average Total Cost curve for a monopolist with points provided by users
      Q1_ATC_monopoly=int(input("Please enter the quantity value of the first data point on the Average Total Cost."))
      P1_ATC_monopoly=int(input("Please enter the price value of the first data point on the Average Total Cost."))

      Q2_ATC_monopoly=int(input("Please enter the quantity value of the 2nd data point on the Average Total Cost."))
      P2_ATC_monopoly=int(input("Please enter the price value of the 2nd data point on the Average Total Cost."))

      Q3_ATC_monopoly=int(input("Please enter the quantity value of the 3rd data point on the Average Total Cost."))
      P3_ATC_monopoly=int(input("Please enter the price value of the 3rd data point on the Average Total Cost."))



      # Instantiation & Invoking function of the monopolist     
      Line_D_monopoly = Line(point1_demand_monopoly, point2_demand_monopoly)  
      print ("The Demand curve for the Monopolist is  P=", Line_D_monopoly.slope, "q+",Line_D_monopoly.intercept)
      
      Line_MC_monopoly= Line(point1_MC_monopoly, point2_MC_monopoly)  
      print ("The Marginal Cost curve for the Monopolist is  P=", Line_MC_monopoly.slope, "q+ ","(",Line_MC_monopoly.intercept,")")

      print("The equilibrium quantity is approximately: ", GetIntersection_monopoly(Line_D_monopoly, Line_MC_monopoly), " units")

      a_monopoly,b_monopoly,c_monopoly=GetQuadraticEquation(Q1_ATC_monopoly,P1_ATC_monopoly, Q2_ATC_monopoly, P2_ATC_monopoly, Q3_ATC_monopoly, P3_ATC_monopoly)
      print("The equation for Average Total Cost is: ",a_monopoly, 'q^2 +',b_monopoly,'q +',c_monopoly,'=P')


      # Calculating Profits/Loss
      
      
      ATC_Qe_pc=a_monopoly * equilibrium_Q**2 + b_monopoly* equilibrium_Q + c_monopoly
      EquilibriumPrice_Qe=Line_D_monopoly.slope * equilibrium_Q + Line_D_monopoly.intercept


      Profit= (EquilibriumPrice_Qe - ATC_Qe_pc)* equilibrium_Q

      if Profit>0:
          print ("Your firm is making ", Profit, "$ of Economic Profit")
      elif Profit<0:
          print ("Your firm is incuring ", Profit, "$ of Economic Loss")


      
      #Graphing the curves
      
      n = 80
      x= np.arange(0, n)

      # Demand Curve of the monopolist
      y4= Line_D_monopoly.slope * x + Line_D_monopoly.intercept
    
      # Marginal revenue curve of the monopolist 
      y5= 2*Line_D_monopoly.slope * x + Line_D_monopoly.intercept

      # MC curve of the monopolist
      y6= Line_MC_monopoly.slope * x + Line_MC_monopoly.intercept

      # ATC curve of the monopolist
      y7= a_monopoly* x **2 + b_monopoly*x + c_monopoly

    
      plt.plot(x,y4)
      plt.plot(x,y5)
      plt.plot(x,y6)
      plt.plot(x,y7)
      plt.show()





