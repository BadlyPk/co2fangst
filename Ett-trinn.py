# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""
import numpy as np
import constants6 as c

m9 = 84.63
T_inn = 298
p_inn = 2
p_ut = 20
T_ut_slutt = 303
p_ut_slutt = 20

cpCO2 = (((c.cpg[0]*1000))/1000)*c.Mw[0]
gamma = cpCO2/(cpCO2-c.gasConst)

T_ut = T_inn*(p_ut/p_inn)**((gamma-1)/gamma)
Ws_rev = m9*(c.cpg[0]*1000)*(T_ut-T_inn)
Ws_real = Ws_rev/c.eta
To_real = T_ut+(Ws_real/(m9*(c.cpg[0]*1000)))
Q_kjoler = m9*(c.cpg[0]*1000)*(T_inn-To_real)

print("Ws_real:", round(Ws_real/1000,3), "kJ/s")
print("Q_kjøler:", round(Q_kjoler/1000,2), "kJ")