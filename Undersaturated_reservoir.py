
from Variables import *
from PVT import *
import numpy as np


NpN_UR = (Bo_UR[0] * Coe * (Pi - P_UR)) / Bo_UR # Fractional oil recovery, %

rw = Xhf / 2

J_UR = (Fhf + K2 * h) / (141.2 * (Uo_UR * Bo_UR) * np.log((reh / rw) - 0.5 + S)) 

qo_UR = J_UR * (P_UR - Pwf) * W # Oil rate, STB/D

Np_UR = NpN_UR * N # Oil recovery, MMSTBO

diff_Np = np.diff(Np_UR)

diff_qo_UR = np.diff(qo_UR)

a = -365*(diff_qo_UR / diff_Np) / 1000000

b = qo_UR[1:] / qo_UR[:-1]

delta_t = np.log(b) / (-a)

t_UR = np.cumsum(delta_t) 

t_UR = np.insert(t_UR,0,0) # time, Years

qg_UR = qo_UR * 671.38 / 1000000 # Gas rate, MMSCF/D

delta_t = np.insert(delta_t,0,0)

delta_Gp = 365 * delta_t * qg_UR

Gp_UR = np.cumsum(delta_Gp) # Cumulative gas production, MMSCF







 



    







