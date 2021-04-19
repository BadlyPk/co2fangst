# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""

import constants6 as c
import scipy.integrate


def CpMEA(T, wMEA):
    CpInt = (1-wMEA)*(c.Aw+c.Bw*T+c.Cw*T**2) + wMEA*(c.Aa+c.Ba*T+c.Ca*T**2) + wMEA*(1-wMEA)*(c.As+c.Bs*T+c.Cs*wMEA*(T)**(-1.5859))
    return CpInt

def CpCO2(T,wMEA,wH2O,wCO2):
    cp = (wH2O+wMEA)*((1-wMEA)*(c.Aw+c.Bw*T+c.Cw*T**2)+wMEA*(c.Aa+c.Ba*T+c.Ca*T**2)+wMEA*(1-wMEA)*(c.As+c.Bs*T+c.Cs*wMEA*(T)**(-1.5859))+wCO2*(c.Ac+c.Bc*T))
    return cp

def CpCO2Int(cp,T0,T,wMEA,wH2O,wCO2):
    cp = scipy.integrate.quad(cp,T0,T,args=(wMEA,wH2O,wCO2))
    return cp[0]
