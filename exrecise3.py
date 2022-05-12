#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 11 22:54:54 2022

@author: lxd972
"""

import numpy as np
import gurobipy as gp
from gurobipy import GRB




def Problem12():
    K = 5
    M = 7
    z_K = []
    
    for m in range(M):
        q_O = 1.2
        q_B = np.random.uniform(1.5,2.2,K)
        d = np.random.uniform(80,120,K)
        m = gp.Model("Problem2")
        x_SH = m.addVar(vtype = GRB.CONTINUOUS, name = "the amount shipped from the factory")
        y_B = m.addVars([i for i in range(K)], vtype = GRB.CONTINUOUS, name = "the amount bought in the local market ")
        y_O = m.addVars([i for i in range(K)], vtype = GRB.CONTINUOUS, name = "the oversupply")
        
        m.setObjective(x_SH + (1/K)*sum(q_B[k]*y_B[k]+q_O*y_O[k] for k in range(K)),GRB.MINIMIZE)
        
        m.addConstr(x_SH <= 100)
        
        
        for k in range(K):
            m.addConstr(y_B[k]-y_O[k]+x_SH == d[k])
        
        m.optimize()
        
        z_K.append(m.getObjective().getValue())
    
    
    z_K = [111.9,119.4,107.8,112.5,111.5,121.2,117.1]
    L_MK = sum(z_K)/M
    
    
    #standard deviation
    theta = (1/(M-1)*sum((z_K[i]-L_MK)**2 for i in range(M)))**(1/2)
    
    #confidence interval (1-10%) = 90%
    
    cinterval = [L_MK-theta*1.29/(M**(1/2)),L_MK+theta*1.29/(M**(1/2))]
        
    print('z_K',z_K)
    print('L_MK',L_MK)
    print('standard deviation',theta)
    print('confidence interval', cinterval)



def Problem4():
    
    m4 = gp.Model("Problem4")
    x_SH = m4.addVars([i for i in range(1,4)],vtype = GRB.CONTINUOUS, name = "the amount shipped from the factory")
    x_ST = m4.addVars([i for i in range(1,4)],vtype = GRB.CONTINUOUS, name = "the amount stored at the factory")
    y_B = m4.addVars([i for i in range(1,8)], vtype = GRB.CONTINUOUS, name = "the amount bought in the local market ")
    y_O = m4.addVars([i for i in range(1,8)], vtype = GRB.CONTINUOUS, name = "the oversupply")
    
    m4.setObjective(x_SH[1] + 0.4*(x_SH[2]+1.5*y_B[2]+1.2*y_O[2]) + 0.6*(x_SH[3]+1.8*y_B[3]+1.3*y_O[3]) + 0.16*(1.65*y_B[4]+1.32*y_O[4]) + 0.24*(1.35*y_B[5]+1.08*y_O[5]) + 0.24*(1.98*y_B[6]+1.43*y_O[6]) + 0.36*(1.62*y_B[7]+1.17*y_O[7]),GRB.MINIMIZE)
    
    # stage 1
    m4.addConstr(x_SH[1] + x_ST[1] == 100)
    
    # stage 2
    m4.addConstr(y_B[2]-y_O[2]+x_SH[1] ==85) 
    
    m4.addConstr(x_SH[2]+x_ST[2]-x_ST[1] ==70)
    
    m4.addConstr(y_B[3]-y_O[3]+x_SH[1] ==115)
    
    m4.addConstr(x_SH[3]+x_ST[3]-x_ST[1] ==70)
    
    # stage 3
    m4.addConstr(y_B[4]-y_O[4]+x_SH[2]+y_O[2] == 93.5)
    
    m4.addConstr(y_B[5]-y_O[5]+x_SH[2]+y_O[2] == 76.5)
    
    m4.addConstr(y_B[6]-y_O[6]+x_SH[3]+y_O[3] == 126.5)
    
    m4.addConstr(y_B[7]-y_O[7]+x_SH[3]+y_O[3] == 103.5)
    
    
    m4.optimize()
            
    print('x_SH:')
    for i in range(1,4):
        print(x_SH[i].x)
        
    print('x_ST:')
    for i in range(1,4):
        print(x_ST[i].x)
    
    print('y_B:')
    for k in range(1,8):
        print(y_B[k].x)
        
    print('y_O:')
    for k in range(1,8):
        print(y_O[k].x)
        


Problem12()
Problem4()



