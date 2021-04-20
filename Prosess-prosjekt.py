import scipy.optimize
def loser(ukjente):
    wcapture = 0.93
    #cv 1
    m1 = 650
    wc1 = 0.14
    wh1 = 0.03
    wn1 = 0.745
    wo1 = 0.085
    #cv2
    wc9 = 1
    wc3 = 0.04107023575638507
    wc4 = 0.09727161100196464
    wc8 = 0.85075

    m2,m3,m4,m6,m8,m9,wc2,wm2,wm3,wm4,wo2,wh2,wn2 = ukjente
    m5 = m4
    wc6 =wc3
    wc5 = wc4
    wm5 = wm4
    wm6 = wm3

    f1 = m2 -m3 + m4 -m1
    f2 = m2*wc2 -m3*wc3 + m4*wc4 - m1*wc1
    f3 = m3*wm3 - wm4*m4
    f4 = m2*wh2- wh1*m1
    f5 = m2*wo2 - wo1*m1
    f6 = m2*wn2 - wn1 *m1
    f7 = m3 - m6
    f8 = m6 + m9 - m5
    f9 = m6*wc6 + m9*wc9 - m5*wc5
    f10 = wc9*m9 - wc1*wcapture*m1
    f11 = m4 - m5
    f12 = m8*wc8 - m9
    f13 = m9+m2-m1
    f14 = m6*wm6 - m5*wm5

    return [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14]

#initial guess
m2_guess = 300.3
m3_guess = 100.3
m4_guess = 50
m6_guess = 100.3
m8_guess = 100
m9_guess = 30
wc2_guess = 0.2
wm2_guess = 0.2
wm3_guess = 0.5
wm4_guess = 0.5
wo2_guess = 0.3
wh2_guess = 0.3

m_guess = [m2_guess,m3_guess,m4_guess,m6_guess, m8_guess,m9_guess, wc2_guess,wh2_guess,wm2_guess,wm3_guess,wm4_guess,wo2_guess,wh2_guess]

sol = scipy.optimize.root(loser,m_guess)
print(sol)


