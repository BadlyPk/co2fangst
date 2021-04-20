# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""

import constants6 as c
from WtFrac import WtFrac

wc3 = WtFrac(c.alpha3,c.Mw[0],c.MwMEA)
wMEA3 = c.waMEA
wh3 = 1-wMEA3 - wc3
wc4 = WtFrac(c.alpha4,c.Mw[0],c.MwMEA)
mt = c.m1

def balanser(x_list):
    w4Mea = x_list[0]
    m2 = x_list[1]
    m3 = x_list[2]
    m4 = x_list[3]
    
    eq1 = m2-m3+m4-mt
    eq2 = wc4*m4 + c.wc1*mt*c.wcapture-wc3*m3-c.wc1*mt
    eq3 = (1-w4Mea-wc4)*m4 - wh3*m3
    eq4 = w4Mea*m4 - wMEA3*m3
    
    eqs = [eq1, eq2, eq3, eq4]
    return eqs
