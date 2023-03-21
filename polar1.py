import numpy as np
import math as m
import matplotlib.pyplot as plt

#disregarding degrees and doing things in radians

lx = input('longitude:').split(" ")
fx = input('lattitude:').split(" ")

s = []
for i in lx:
    j = m.radians(float(i))
    s.append(j)
lx = np.array(s)

s = []
for i in fx:
    j = m.radians(float(i))
    s.append(j)
fx = np.array(s)

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
    l = []
    s = []
    I = input('Inclination:').split(' ')
    for i in I:
        i = m.radians(float(i))
        j = np.arctan(m.tan(i)/2)
        l.append(j)
    l = np.array(l)

else:
    l = input('paleolattitude:').split(' ')
    l = np.array(l)




D = input('Declination:').split(' ')
Z = []
for i in D:
    i = m.radians(float(i))
    Z.append(i)
D = np.array(Z)


def cos_formula(x, y, z):
    return np.arcsin(m.sin(x)*m.sin(y)+m.cos(x)*m.cos(y)*m.cos(z))


LP = np.frompyfunc(cos_formula, 3, 1)

lp = LP(lx, l, D)
print(lp)
print(D)
print(fx)
print(l)
print(lx)
print(len(l))


'''def f_p(x,y,z,w):
    return x + np.arcsin(m.cos(y)*m.sin(z)/m.cos(w))

def f_n(x,y,z,w):
    return fx[i] - m.pi + np.arcsin(m.cos(l[i])*m.sin(D[i])/m.cos(lp[i]))'''

fp = []
for i in range(len(l)):
    if m.sin(l[i])>=m.sin(lp[i])*m.sin(lx[i]):
        f = fx[i] + np.arcsin(m.cos(l[i])*m.sin(D[i])/m.cos(lp[i]))
        fp.append(f)
    else:
        f = fx[i] - np.arcsin(m.cos(l[i])*m.sin(D[i])/m.cos(lp[i]))
        fp.append(f)

fp = np.array(fp)

print(lp, fp)

# s = []
# for i in lp:
#     j = m.degrees(i)
#     s.append(j)
# lp = np.array(s)

# s = []
# for i in fp:
#     j = m.degrees(i)
#     s.append(j)
# fp = np.array(s)

np_deg = np.frompyfunc(m.degrees, 1, 1)
fp = np_deg(fp)
lp = np_deg(lp)

print(lp, fp)
plt.plot(lp, fp)
plt.show()