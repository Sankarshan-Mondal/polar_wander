import numpy as np
import math as m

#disregarding degrees and doing things in radians

lx = m.radians(float(input('longitude:')))
fx = m.radians(float(input('lattitude:')))
'''lp = input('paleolongitude:')
fp = input('paleolattitude:')

b = m.pi/2 - lx
c = m.pi/2 - lp

A = fp - fx

a = np.arccos(m.sin(lx)*m.sin(lp)+m.cos(lx)*m.cos(lp)*m.cos(fp-fx))

C = np.arcsin(m.cos(lp)*m.sin(fp - fx)/m.sin(a))
'''
#v = omega*R*m.sin(a)
#beta = m.pi/2 + C

choice = input('Choose "l" if you have paleolattitude, choose "i" if you have inclination:')

if choice== "i":
    I = m.radians(float(input('Inclination:')))
    l = np.arctan((m.tan(I))/2)
else:
    l = m.radians(float(input('paleolattitude:')))

D = m.radians(float(input('Declination:')))



lp = np.arcsin(m.sin(lx)*m.sin(l)+m.cos(lx)*m.cos(l)*m.cos(D))

if (m.sin(l))>= (m.sin(lp))*(m.sin(lx)):
    fp = fx + np.arcsin(m.cos(l)*m.sin(D)/m.cos(lp))
elif (m.sin(l))<(m.sin(lp))*(m.sin(lx)):
    fp = fx - np.arcsin(m.cos(l)*m.sin(D)/m.cos(lp))

lp = m.degrees(lp)
fp = m.degrees(fp)


print(lp, fp)
