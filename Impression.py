from PVT import*
from Undersaturated_reservoir import*
from Saturated_reservoir import*
import pandas as pd


# PVT Undersaturated reservoir
PVT_UR = {
    "P_UR"  : P_UR,
    "Bo_UR" : Bo_UR,
    "Uo_UR" : Uo_UR
}

df_PVT_UR = pd.DataFrame(PVT_UR)

# PVT Saturated reservoir
PVT_SR = {
    "P_SR"  : P_SR,
    "Bo_SR" : Bo_SR,
    "Uo_SR" : Uo_SR,
    "Bg_SR"  : Bg_SR,
    "Ug_SR" : Bg_SR,
    "Rs_SR" : Rs_SR
}

df_PVT_SR = pd.DataFrame(PVT_SR)


# Variables Undersaturated reservoir
Variables_UR = {
    "P, psi"  : P_UR,
    "Np/N, %": NpN_UR*100,
    "qo, STB/D" : qo_UR,
    "qg, MMSCF/D" : qg_UR,
    "Gp, MMSCF" : Gp_UR,
    "t, Years"  : t_UR  
}

df_Variables_UR = pd.DataFrame(Variables_UR)


# Variables Saturated reservoir
Variables_SR = {
    "P, psi"  : P_SR_,
    "Np/N, %"  : NpN_SR_*100,
    "qo, STB/D" : qo_SR,
    "qg, MMSCF/D" : qg_SR,
    "GOR, SCF/STB"   : GOR_*5.615,
    "Gp, MMSCF" : Gp_SR_,
    "t_Years"  : t_SR
}

df_Variables_SR = pd.DataFrame(Variables_SR)


with pd.ExcelWriter("Results.xlsx") as writer:
    df_PVT_UR.to_excel(writer, sheet_name="PVT_UR", index=False)
    df_PVT_SR.to_excel(writer, sheet_name="PVT_SR", index=False)
    df_Variables_UR.to_excel(writer, sheet_name="UnderSatRes", index=False)
    df_Variables_SR.to_excel(writer, sheet_name="SatRes", index=False)