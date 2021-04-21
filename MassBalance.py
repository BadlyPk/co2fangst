"""
TKP4120 - Prosjekt CO2-fangst

Gruppe 6 - Andrea Skog, Ståle Breimoen, Hanna Imsland Mo, Martin Pham. 

"""

import scipy.optimize
import constants6 as c
import WtFrac as WF
def loser(ukjente):
    wcapture = c.wcapture
    #cv 1
    m1 = c.m1
    wc1 = c.wc1
    wh1 = c.wh1
    wn1 = c.wn1
    wo1 = c.wo1
    #cv2
    wc9 = c.wc9
    wc3 = WF.wc3
    wc4 = WF.wc4
    wc8 = WF.wc8
    wm9 = 0
    wh9 = 0


    

    m2,m3,m4,m8,m9,wc2,wh4,wm4,wh2,wn2,wo2 = ukjente
    wm3 = 0.3 #fra constants.py waMEA = 0.3
    wh3 = 1 - wc3 - wm3

    

    # f1 = m1-m2-m9 #
    f2 = m1-m2+m3-m4 #
    # f3 = m1*wc1 - m1*wc1*(1-wcapture) - m1*wcapture*wc1 +m3*wc3 #
    f4 = m1*wh1 - m2*wh2 #
    f5 = m1*wn1 - m2*wn2 #
    # f6 = m4 - m3 - wc1*wcapture*m1 #???
    f7 = m4*wc4 - m3*wc3 - m9*wc9 #bytt ut m4*wc4 med m1*wcapture*wc1 ???
    f8 = m4 - m3 - m9 #
    # f9 = m4*wc4 - m9*wc9 - m3*wc3 #
    # f10 = m4*wh4 - m9*wh9 - m3*wh3 #???
    f11 = m4*wm4 - m9*wm9 - m3*wm3 #
    f12 = m8 - m9*wc9 - m8*(1-wc8)

    # f13 = m8*wc8 - m9*wc9 #
    f15 = m1*wo1 - m2*wo2 #
    # f16 = m4*wc4 - m1*wcapture*wc1
    f17 = 1-wc2-wn2-wh2-wo2
    # f18 = 1- wh3 - wc3 - wm3
    f19 = wc2 - m1*wc1*(1-wcapture)/m2
    f20 = 1 - wm4 - wc4 - wh4


    return [f2,f4,f5,f7,f8,f11,f12,f17,f15,f19,f20]

#initial guess
m2_guess = 600
m3_guess = 100
m4_guess = 150
m8_guess = 100
m9_guess = 50
wc2_guess = 0.25
wh4_guess = 0.2
wm4_guess = 0.2
wh2_guess = 0.25
wn2_guess = 0.25
wm3_guess = 0.2
wh3_guess = 0.2
wo2_guess = 0.25

m_guess = [m2_guess,m3_guess,m4_guess, m8_guess,m9_guess, wc2_guess,wh3_guess,wh4_guess,wm4_guess,wh2_guess,wn2_guess]

sol = scipy.optimize.root(loser,m_guess)
print(sol)

losn = []
for i in range(11):
    losn.append(round(sol["x"][i],3)) 

m2,m3,m4,m8,m9,wc2,wh4,wm4,wh2,wn2,wo2 = losn

print(
    f"m1 = {c.m1}\n"
    f"m2 = {m2}\n" 
    f"m3 = {m3}\n"
    f"m4 = {m4}\n"
    f"m5 = {m4}\n"
    f"m6 = {m3}\n"
    f"m7 = {m3}\n"
    f"m8 = {m8}\n"
    f"m9 = {m9}\n"

    f"wc1 = {round(c.wc1,3)}\n"
    f"wh1 = {round(c.wh1,3)}\n"
    f"wn1 = {round(c.wn1,3)}\n"
    f"wo1 = {round(c.wo1,3)}\n"

    f"wc2 = {wc2}\n"
    f"wh2 = {wh2}\n"
    f"wn2 = {wn2}\n"
    f"wo2 = {wo2}\n"

    f"wc3 = {round(WF.wc3,3)}\n"
    f"wm3 = {c.waMEA}\n"
    f"wh3 = {round(1 - WF.wc3 - c.waMEA,3)}\n"
    
    f"wh4 = {wh4}\n"
    f"wm4 = {wm4}\n"
    f"wc4 = {round(WF.wc4,3)}\n"

    f"wc8 = {round(WF.wc8,3)}\n"
    f"wh8 = {round(1-WF.wc8,3)}\n"
)