#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:00:24 2022

@author: lxd972
"""
import gurobipy as gp
from gurobipy import GRB


m = gp.Model("Problem6")
#self.m.Params.TimeLimit = 300
#self.m.Params.MIPGap = 0.0
x_SH = m.addVar(vtype = GRB.INTEGER, name = "the amount shipped from the factory")
y_B = m.addVars([i for i in range(1,4)], vtype = GRB.INTEGER, name = "the amount bought in the local market ")
y_O = m.addVars([i for i in range(1,4)], vtype = GRB.INTEGER, name = "the oversupply")

m.setObjective(x_SH + 0.3*(1.5*y_B[1]+1.2*y_O[1]) + 0.3*(1.7*y_B[2]+1.2*y_O[2])+0.4*(2*y_B[3]+1.2*y_O[3]),GRB.MINIMIZE)

m.addConstr(x_SH <= 100)
m.addConstr(y_B[1]-y_O[1]+x_SH == 85)
m.addConstr(y_B[2]-y_O[2]+x_SH == 105)
m.addConstr(y_B[3]-y_O[3]+x_SH == 120)

m.optimize()
        
print('x_SH:',x_SH.x)

print('y_B:')
for i in range(1,4):
    print(y_B[i].x)
    
print('y_O:')
for i in range(1,4):
    print(y_O[i].x)
    
    
    