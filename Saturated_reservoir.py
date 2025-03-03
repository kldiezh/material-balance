
from Variables import *
from PVT import *
from Undersaturated_reservoir import*
import numpy as np

def calcular_A1():
     return Bo_SR / Bg_SR - Rs_SR

def calcular_B1():
    return 1 / Bg_SR

A1  = calcular_A1()
B1  = calcular_B1()

NpNb = NpN_UR[len(NpN_UR)-1] # Previous Fractional oil recovery

NpN_fijo = NpN_UR[len(NpN_UR)-1] # Seed

NpNk = NpN_fijo

So_= np.array([])
Sg_= np.array([])
GOR_ = np.array([])
NpN_SR_ = np.array([])
J_SR_ = np.array([])

maxiter = 1000

GOR = Rs_SR[0]

print('P_SR[i] \t So \t Sg \t GOR')

# Iterative cycle to calculate pressure

for i in range(1,len(P_SR)):
     
     iter, error = 0, 1

     NpN = NpNk

     while error>=0.000001 and iter<maxiter:
        iter += 1
          
        Npfa = (NpN - NpNb) / (1 - NpNb)
        
        So = (1 - Npfa) * (Bo_SR[i] / Bob) * (1 - Sw)
        Sg = 1 - So - Sw

        S = Sg / (1 - Sor - Sw)
        Krg = S * Krgc
        Kro = (1 - S) * Kroc

        GORk = (Rs_SR[i] + (Krg * Uo_SR[i] * Bo_SR[i]) / (Kro * Ug_SR[i] * Bg_SR[i]))
        
        A = (1 - NpN) * (A1[i] - A1[i - 1])
           
        B = Bob * (1 + m) * (B1[i] - B1[i-1])
    
        DiffP = P_SR[i] - P_SR[i - 1]
    
        C = 1 + (((1 - W) * C1 + W * C2) * DiffP)
    
        AVG_GOR = (GORk + GOR)/2
        
        D = (Bo_SR[i] / Bg_SR[i] - Rs_SR[i]) + AVG_GOR * (1 - Ig)
    
        DiffNp = (A - B * C) / D 

        error = np.abs(NpNk - (DiffNp + NpN))/np.abs((DiffNp + NpN))

        NpNk = DiffNp + NpN_fijo

        NpN = NpNk

        J_SR = (J_UR[0] * Kro * Uo_UR[0] * Bo_UR[0]) / (1 * Uo_SR[i] * Bo_SR[i]) 
   
  
     NpN_fijo = NpNk 
     GOR = GORk

     So_ = np.append(So_, So)
     Sg_ = np.append(Sg_, Sg)
     GOR_ = np.append(GOR_, GORk)
     J_SR_ = np.append(J_SR_, J_SR)
     NpN_SR_ = np.append(NpN_SR_, NpNk)


     print(f'{P_SR[i]} \t {So} \t {Sg} \t {GOR}')

P_SR_ = P_SR[1:]

qo_SR = J_SR * (P_SR_- Pwf) * W # Oil rate, STB/D

Np_SR = NpN_SR_ * N # Oil recovery, MMSTBO

diff_Np_ = np.diff(Np_SR)

diff_qo_SR = np.diff(qo_SR)

a_ = -365 * (diff_qo_SR/diff_Np_)/1000000

b_ = qo_SR[1:] / qo_SR[:-1]

delta_t_ = np.log(b_) / (-a_)

t_SR = np.cumsum(delta_t_) + t_UR[len(t_UR)-1]

t1 = (t_UR[len(t_UR)-1] + t_SR[0]) / 2

t_SR = np.insert(t_SR,0,t1) # time, Years

qg_SR = qo_SR * GOR_ * 5.615 / 1000000 # Gas rate, MMSCF/D

delta_t_ = np.insert(delta_t_,0,0)

delta_Gp_ = 365 * delta_t_ * qg_SR

Gp_SR_ = np.cumsum(delta_Gp_) + Gp_UR[len(Gp_UR) - 1] # Cumulative gas production, MMSCF














