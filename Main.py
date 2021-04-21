# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""
import numpy as np
import scipy.integrate
import scipy.optimize
import constants6 as c
import CpSol
import Massebalanser as mb
from Enthalpy import enthalpy
from WtFrac import WtFrac

wc3 = WtFrac(c.alpha3,c.Mw[0],c.MwMEA)
wMEA3 = c.waMEA
wh3 = 1-wMEA3-wc3
wc4 = WtFrac(c.alpha4,c.Mw[0],c.MwMEA)
mt = c.m1

guess = [0,500,250,290]
mass = scipy.optimize.root(mb.balanser,guess)

wMEA4 = mass.x[0]
m2 = mass.x[1]
m3 = mass.x[2]
m4 = mass.x[3]
m5 = m4
m6 = m3
m7 = m3
m9 = m5-m6
mt = c.m1

wc2 = c.m1*c.wc1*(1-c.wcapture)/m2
wn2 = c.wn1*c.m1/m2
wo2 = c.wo1*c.m1/m2
wh2 = 1-wn2-wo2-wc2
wh4 = 1-wMEA4-wc4
wc8 = c.xc8*c.Mw[0]/(c.xc8*c.Mw[0]+(1-c.xc8)*c.Mw[1])
m8 = m9/wc8

m = [c.m1,m2,m3,m4,m5,m6,m7,m8,m9]

cp1 = c.wc1*c.cpg[0]+c.wh1*c.cpg[1]+c.wn1*c.cpg[2]+c.wo1*c.cpg[3]
h1 = c.wc1*c.hf[0]+c.wh1*c.hf[1]+c.wn1*c.hf[2]+c.wo1*c.hf[3]+cp1*(c.T[0]-c.Tref_C)
H1 = h1*c.m1

cp2 = wc2*c.cpg[0]+wh2*c.cpg[1]+wn2*c.cpg[2]+wo2*c.cpg[3]
h2 = wc2*c.hf[0]+wh2*c.hf[1]+wn2*c.hf[2]+wo2*c.hf[3]+cp2*(c.T[1]-c.Tref_C)
H2 = h2*c.m1

CO2abs_367 = wc3*m3/c.Mw[0]*1000
Habs_367 = CO2abs_367*c.habs_m

CO2abs_45 = wc4*m4/c.Mw[0]*1000
Habs_45 = CO2abs_45*c.habs_m

Qv1 = m4*CpSol.CpCO2Int(CpSol.CpCO2,c.T[3]+273.15,c.T[4]+273.15,wMEA4,wh4,wc4)

def findT7(x_list):
    T7 = x_list[0]
    TO = c.T[5]+273.15
    
    wMEA = c.waMEA
    
    subeq1 = (1-wMEA)*(c.Aw*(T7-TO)+(1/2)*c.Bw*(T7**2-TO**2)+(1/3)*c.Cw*(T7**3-TO**3))
    subeq2 = wMEA*(c.Aa*(T7-TO)+(1/2)*c.Ba*(T7**2-TO**2)+(1/3)*c.Ca*(T7**3-TO**3))
    subeq3 = wMEA*(1-wMEA)*(c.As*(T7-TO)+(1/2)*c.Bs*(T7**2-TO**2)-1.589*c.Cs*wMEA*(T7-273.15)**(-0.5859))
    subeq4 = wc3*(c.Ac*(T7-TO)+(1/2)*c.Bc*(T7**2-TO**2))
    
    toteq = m3*((wMEA+wh3)*(subeq1+subeq2+subeq3)+subeq4) + Qv1
    return toteq

T69 = 420
T7 = scipy.optimize.root(findT7,T69)

c.T[6] = T7.x[0]-273.15

H3 = enthalpy(c.Tref_C,c.T[2],c.waMEA,wc3,wh3,Habs_367,m3)
H4 = enthalpy(c.Tref_C,c.T[3],wMEA4,wc4,wh4,Habs_45,m4)
H5 = enthalpy(c.Tref_C,c.T[4],wMEA4,wc4,wh4,Habs_45,m4)
H6 = enthalpy(c.Tref_C,c.T[5],c.waMEA,wc3,wh3,Habs_367,m3)
H7 = enthalpy(c.Tref_C,c.T[6],c.waMEA,wc3,wh3,Habs_367,m3)

dt_LN = ((c.T[6]-c.T[3])-(c.T[5]-c.T[4]))/np.log((c.T[6]-c.T[3])/(c.T[5]-c.T[4]))
A = Qv1*1000/(dt_LN*c.U)

Qv2 = m3*CpSol.CpCO2Int(CpSol.CpCO2,c.T[6]+273.15,c.T[2]+273.15,c.waMEA,wh3,wc3)

h_vap = c.dHfus-c.dHsub
wh8 = 1-wc8
Qv3 = m8*(-h_vap*wh8-wh8*c.cpg[1]*(c.T[7]-c.Tref_C)-wc8*c.cpg[0]*(c.T[7]-c.Tref_C))

Cp8 = wc8*c.cpg[0]+wh8*c.cpg[1]
h8 = wc8*c.hf[0]+wh8*c.hf[1]+Cp8*(c.T[7]-c.Tref_C)
H8 = h8*m8

H9 = m9*c.hf[0]

H = [H1,H2,H3,H4,H5,H6,H7,H8,H9]
h = [H1/c.m1,H2/m2,H3/m3,H4/m4,H5/m5,H6/m6,H7/m7,H8/m8,H9/m9]

Qv4 = Qv3+H9+H6-H5
Q = [Qv1,Qv2,Qv3,Qv4]


print("T7:", T7)
print("---")
print("Entalpi:", h)
print("---")
print("Masser:", m)
print("---")
print("Varmeoverføring:", Q)
print("---")


