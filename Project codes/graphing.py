import matplotlib.pyplot as plt
import numpy as np
import Project_main

def pc_firm ():
    #x range
    n = 60
    x= np.arange(0, n)
    
    # Demand, Marginal revenue curve of the pc firm
    y1= Line_MR_pc.slope * x + Line_MR_pc.intercept

    # MC curve of the pc firm
    y2= Line_MC_pc.slope * x + Line_MC_pc.intercept

    # ATC curve of the pc firm
    y3= a*x **2 + b*x + c


    plt.plot(x,y1)
    plt.plot(x,y2)
    plt.plot(x,y3)
    plt.show()
 

def monopolist ():

    #x range
    n = 60
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



if (m==1):
    pc_firm()
elif (m==2):
    monopolist()

