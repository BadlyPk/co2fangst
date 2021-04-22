# -*- coding: utf-8 -*-
"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""
import numpy as np
import constants6 as c

MmCO2 = 44.01
cpCO2 = ((c.cpg[0])/1000)*MmCO2
m9 = 84.63
gamma = cpCO2/(cpCO2-c.gasConst)

#Første trinn
T_inn1 = 298
p_inn1 = 2
p_ut1 = 4
T_ut1 = T_inn1*(p_ut1/p_inn1)**((gamma-1)/gamma)
Ws_rev1 = m9*(c.cpg[0]*1000)*(T_ut1-T_inn1)
Ws_real1 = Ws_rev1/c.eta
To_real1 = T_ut1+(Ws_real1/(m9*(c.cpg[0]*1000)))
Q_kjoler1 = m9*(c.cpg[0]*1000)*(T_inn1-To_real1)

print("Første trinn:")
print("Ws_real:", round(Ws_real1/1000,3), "kJ/s")
print("Q_kjøler:", round(Q_kjoler1/1000,2), "kJ")
print("---")

#Andre trinn
T_inn2 = 303
p_inn2 = 4
p_ut2 = 8
T_ut2 = T_inn2*(p_ut2/p_inn2)**((gamma-1)/gamma)
Ws_rev2 = m9*(c.cpg[0]*1000)*(T_ut2-T_inn2)
Ws_real2 = Ws_rev2/c.eta
To_real2 = T_ut2+(Ws_real2/(m9*(c.cpg[0]*1000)))
Q_kjoler2 = m9*(c.cpg[0]*1000)*(T_inn2-To_real2)

print("Andre trinn:")
print("Ws_real:", round(Ws_real2/1000,3), "kJ/s")
print("Q_kjøler:", round(Q_kjoler2/1000,2), "kJ")
print("---")

#Tredje trinn
T_inn3 = 303
p_inn3 = 8
p_ut3 = 20
T_ut3 = T_inn3*(p_ut3/p_inn3)**((gamma-1)/gamma)
Ws_rev3 = m9*(c.cpg[0]*1000)*(T_ut3-T_inn3)
Ws_real3 = Ws_rev3/c.eta
To_real3 = T_ut3+(Ws_real3/(m9*(c.cpg[0]*1000)))
Q_kjoler3 = m9*(c.cpg[0]*1000)*(T_inn3-To_real3)

print("Tredje trinn:")
print("Ws_real:", round(Ws_real3/1000,3), "kJ/s")
print("Q_kjøler:", round(Q_kjoler3/1000,2), "kJ")
print("---")
