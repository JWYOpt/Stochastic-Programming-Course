#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 13:09:34 2022

@author: lxd972
""" 

import numpy as np
import gurobipy as gp
from gurobipy import GRB

def Exercise3():
    
    m = gp.Model("Exercise 3")
    x_SH = m.addVars([i for i in range(1,3)],[j for j in range(1,5)],vtype = GRB.CONTINUOUS, name = "the amount shipped from the factory")
    x_ST = m.addVars([i for i in range(1,3)], [j for j in range(1,5)],vtype = GRB.CONTINUOUS, name = "the amount stored at the factory")
    y_B = m.addVars([i for i in range(2,4)], [j for j in range(1,5)],vtype = GRB.CONTINUOUS, name = "the amount bought in the local market ")
    y_O = m.addVars([i for i in range(2,4)], [j for j in range(1,5)],vtype = GRB.CONTINUOUS, name = "the oversupply")
    
    m.setObjective(0.16*(x_SH[1,1] + x_SH[2,1]+1.5*y_B[2,1]+1.2*y_O[2,1]+1.65*y_B[3,1]+1.32*y_O[3,1]) + 0.24*(x_SH[1,2]+x_SH[2,2]+1.5*y_B[2,2]+1.2*y_O[2,2]+1.35*y_B[3,2]+1.08*y_O[3,2]) + 0.36*(x_SH[1,3]+x_SH[2,3]+1.8*y_B[2,3]+1.3*y_O[2,3]+1.98*y_B[3,3]+1.43*y_O[3,3]) + 0.24*(x_SH[1,4]+x_SH[2,4]+1.8*y_B[2,4]+1.3*y_O[2,4]+1.62*y_B[3,4]+1.17*y_O[3,4]) ,GRB.MINIMIZE)
    
    # Constraints scenario 1
    m.addConstr(x_SH[1,1] + x_ST[1,1] == 100)
    
    m.addConstr(y_B[2,1]-y_O[2,1]+x_SH[1,1] ==85) 
    
    m.addConstr(x_SH[2,1]+x_ST[2,1]-x_ST[1,1] ==70)
    
    m.addConstr(y_B[3,1]-y_O[3,1]+x_SH[2,1] + y_O[2,1] ==93.5)

    # Constraints scenario 2
    m.addConstr(x_SH[1,2] + x_ST[1,2] == 100)
    
    m.addConstr(y_B[2,2]-y_O[2,2]+x_SH[1,2] ==85) 
    
    m.addConstr(x_SH[2,2]+x_ST[2,2]-x_ST[1,2] ==70)
    
    m.addConstr(y_B[3,2]-y_O[3,2]+x_SH[2,2] + y_O[2,2] ==76.5)
    
    # Constraints scenario 3
    m.addConstr(x_SH[1,3] + x_ST[1,3] == 100)
    
    m.addConstr(y_B[2,3]-y_O[2,3]+x_SH[1,3] ==115) 
    
    m.addConstr(x_SH[2,3]+x_ST[2,3]-x_ST[1,3] ==70)
    
    m.addConstr(y_B[3,3]-y_O[3,3]+x_SH[2,3] + y_O[2,3] ==126.5)
    
    # Constraints scenario 4
    m.addConstr(x_SH[1,4] + x_ST[1,4] == 100)
    
    m.addConstr(y_B[2,4]-y_O[2,4]+x_SH[1,4] ==115) 
    
    m.addConstr(x_SH[2,4]+x_ST[2,4]-x_ST[1,4] ==70)
    
    m.addConstr(y_B[3,4]-y_O[3,4]+x_SH[2,4] + y_O[2,4] ==103.5)
    
    # NACs stage 1
    m.addConstr(x_SH[1,1] - x_SH[1,2] == 0)
    
    m.addConstr(x_SH[1,1] - x_SH[1,3] == 0)
    
    m.addConstr(x_SH[1,1] - x_SH[1,4] == 0)
    
    m.addConstr(x_ST[1,1] - x_ST[1,2] == 0)

    m.addConstr(x_ST[1,1] - x_ST[1,3] == 0) 
    
    m.addConstr(x_ST[1,1] - x_ST[1,4] == 0) 
    
    # NACs stage 2
    m.addConstr(x_SH[2,1] - x_SH[2,2] == 0)
    
    m.addConstr(x_SH[2,3] - x_SH[2,4] == 0)
    
    m.addConstr(x_ST[2,1] - x_ST[2,2] == 0)

    m.addConstr(x_ST[2,3] - x_ST[2,4] == 0)    
    
    m.addConstr(y_B[2,1] - y_B[2,2] == 0)
    
    m.addConstr(y_B[2,3] - y_B[2,4] == 0)
    
    m.addConstr(y_O[2,1] - y_O[2,2] == 0)

    m.addConstr(y_O[2,3] - y_O[2,4] == 0) 
    
   
    
    m.optimize()
            
    # print('x_SH:')
    for i in range(1,3):
        for j in range(1,5):
            print('x_SH[',i,j, ']',x_SH[i,j].x)
        
    # print('x_ST:')
    for i in range(1,3):
        for j in range(1,5):
            print('x_ST[',i,j,']',x_ST[i,j].x)
    
    # print('y_B:')
    for i in range(2,4):
        for j in range(1,5):
            print('y_B[',i,j,']',y_B[i,j].x)
        
    # print('y_O:')
    for i in range(2,4):
        for j in range(1,5):
            print('y_O[',i,j,']',y_O[i,j].x)
        


Exercise3()



