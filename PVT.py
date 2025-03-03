
from Variables import *
import numpy as np 
import pandas as pd

P = np.arange(Pi,2180,-20) # Pressure array

P_UR = np.array([]) # Pressures above Pb.
P_SR = np.array([]) # Presssure below Pb.

for num in P:
    if num >= Pb:
        P_UR = np.append(P_UR, num)
    if num <= Pb:
        P_SR = np.append(P_SR, num)

# PVT for Undersaturated Reservoir

def calcular_Bo_UR(P_UR):
    return -0.00001529 * P_UR + 1.47725786

def calcular_Uo_UR(P_UR):
    return 0.0000554429 * P_UR + 0.4645469286

Bo_UR = calcular_Bo_UR(P_UR)
Uo_UR = calcular_Uo_UR(P_UR)

# PVT for Saturated Reservoir

def calcular_Bo_SR(P_SR):
    return 0.00011448 * P_SR + 1.16638115

def calcular_Bg_SR(P_SR):
    return 20.40472 * np.power(P_SR, -1.02454)

def calcular_Uo_SR(P_SR):
    return 0.0000000907 * np.power(P_SR, 2) - 0.0003674172 * P_SR + 0.9616952608

def calcular_Ug_SR(P_SR):
    return 0.00000236 * P_SR + 0.01241004

def calcular_Rs_SR(P_SR):
    return 0.04285545 * P_SR + 15.67415590

Bo_SR = calcular_Bo_SR(P_SR)
Bg_SR = calcular_Bg_SR(P_SR)
Uo_SR = calcular_Uo_SR(P_SR)
Ug_SR = calcular_Ug_SR(P_SR)
Rs_SR = calcular_Rs_SR(P_SR)































     














