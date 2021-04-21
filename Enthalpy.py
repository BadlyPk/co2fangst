# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""

import scipy.integrate as integrate
import CpSol
import constants6 as c

def enthalpy(Tref,T,wMEA,wCO2,wH2O,Habs,m):
    SolH = integrate.quad(CpSol.CpMEA,Tref+273.15,T+273.15,args=wMEA)[0]
    CO2H = integrate.quad(CpSol.CpCO2,Tref,T,args=(wMEA,wCO2,wH2O))[0]
    H = m*(wMEA+wH2O)*(c.hfsol+SolH)+wCO2*(c.hf[0]+CO2H)+wCO2*Habs
    return H