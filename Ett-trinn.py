# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""
import numpy as np

T_inn = 298

MmCO2 = 44.01
p_inn = 2
p_ut = 20
T_ut_slutt = 303
p_ut_slutt = 20

cpCO2_ubrukt = 0.868*1000
cpCO2 = ((cpCO2_ubrukt)/1000)*MmCO2
m9 = 6
eta = 0.85
R = 8.314
gamma = cpCO2/(cpCO2-R)

T_ut = T_inn*(p_ut/p_inn)**((gamma-1)/gamma)
Ws_rev = m9*cpCO2_ubrukt*(T_ut-T_inn)
Ws_real = Ws_rev/eta
To_real = T_ut+(Ws_real/(m9*cpCO2_ubrukt))
Q_kjoler = m9*cpCO2_ubrukt*(T_inn-To_real)

print(round(Ws_real/1000,3), "kJ/s")
print(round(Q_kjoler/1000,2), "kJ")