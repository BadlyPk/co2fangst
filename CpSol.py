# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""

import constants6 as c
import scipy.integrate

def CpMEA(T, wMEA):
    CpInt = (1-wMEA)*(c.Aw+c.Bw*T+c.Cw*(T+273.15)**2) + wMEA*(c.Aa+c.Ba*T+c.Ca*(T+273.15)**2) + wMEA*(1-wMEA)*(c.As+c.Bs*T+c.Cs*wMEA*(T)**(-1.5859))
    return CpInt

def CpCO2(T,wMEA,wH2O,wCO2):
    cp = (wH2O+wMEA)*((1-wMEA)*(c.Aw+c.Bw*(T+273.15)+c.Cw*(T+273.15)**2)+wMEA*(c.Aa+c.Ba*(T+273.15)+c.Ca*(T+273.15)**2)+wMEA*(1-wMEA)*(c.As+c.Bs*(T+273.15)+c.Cs*wMEA*(T)**(-1.5859))+wCO2*(c.Ac+c.Bc*(T+273.15)))
    return cp

def CpCO2Int(cp,T0,T,wMEA):
    cp = scipy.integrate.quad(cp,T0,T,args=(wMEA))
    return cp[0]


def cpmea(T):
    return c.Aa + c.Ba * (T) + c.Ca * (T)**2

def cpco2(T):
    return c.Ac + c.Bc * (T) 

def cph2o(T):
    return c.Aw + c.Bw * (T) + c.Cw * (T)**2

def cpsol(T,wMEA):
    return (1-wMEA) *cph2o(T) + wMEA * cpmea(T) + wMEA*(1-wMEA)*( c.As + c.Bs*(T) + c.Cs*wMEA*(T)**(-1.5859))

def Intcpsol(T,wMEA):
    return (1-wMEA)* ( c.Aw * T + c.Bw *0.5* (T)**2 + c.Cw * (T)**3 / 3) + wMEA * (c.Aa*T + c.Ba * (T)**2 /2 + c.Ca * (T)**3 /3) + wMEA*(1-wMEA)*( c.As*T + c.Bs*(T)**2 /2 + c.Cs*wMEA*(-1.70679/(T-273.15)**0.5859))

