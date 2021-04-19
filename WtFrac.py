# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""
import constants6 as c

def WtFrac(alpha, MwCO2, MwMEA):
    WtFrac = MwCO2*alpha/((1+0.7/0.3)*MwMEA)
    return WtFrac



wc3 = WtFrac(c.alpha3,c.Mw[0],c.MwMEA)
wMEA3 = c.waMEA
wh3 = 1-wMEA3-wc3
wc4 = WtFrac(c.alpha4,c.Mw[0],c.MwMEA)