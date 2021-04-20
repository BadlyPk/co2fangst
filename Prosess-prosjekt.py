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
    wm9 = 0
    wh9 = 0


    

    m2,m3,m4,m8,m9,wc2,wh3,wh4,wm4,wh2,wn2,wm3 = ukjente

    f1 = m1-m2-m9 #
    f2 = m1-m2+m3-m4 #
    f3 = m1*wc1 - m2*wc2 - wc1*wcapture*m1 +m3*wc3 #
    f4 = m1*wh1 - m2*wh2 #
    f5 = m1*wn1 - m2*wn2 #
    # f6 = m4 - m3 - wc1*wcapture*m1#???
    f7 = m4*wc4 - m3*wc3 - wc1*wcapture*m1 - m3*wc3
    f8 = m4 - m3 - m9 #
    f9 = m4*wc4 - m9*wc9 - m3*wc3 #
    f10 = m4*wh4 - m9*wh9 - m3*wh3 #???
    f11 = m4*wm4 - m9*wm9 - m3*wm3 #
    f12 = m8 - m8*wc8 - m8*(1-wc8)

    f13 = m8*wc8 - m9*wc9 #
    # f15 = m1*wo1 - m2*wo2 #

    return [f1,f2,f3,f4,f5,f7,f8,f9,f10,f11,f12,f13]

#initial guess
m2_guess = 300.3
m3_guess = 100.3
m4_guess = 50
m8_guess = 100
m9_guess = 30
wc2_guess = 0.2
wh4_guess = 0.2
wm4_guess = 0.5
wh2_guess = 0.5
wn2_guess = 0.3
wm3_guess = 0.3
wh3_guess = 0.3
wo2_guess = 0.3

m_guess = [m2_guess,m3_guess,m4_guess, m8_guess,m9_guess, wc2_guess,wh3_guess,wh4_guess,wm4_guess,wh2_guess,wn2_guess,wm3_guess]

sol = scipy.optimize.root(loser,m_guess)
print(sol)


