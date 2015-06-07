import pylab as plt
import numpy as np

R = 1
lamda = 500E-9
#d = 50E-6
scn = 1E-6
tms = 500
rds_tm = 25
rds = scn*rds_tm

side = np.linspace(-scn*tms,scn*tms,tms)
x,y = np.meshgrid(side, side)

# The circular aperture w/ radius == 50 um
E_ca = x**2+y**2 < rds**2

D1 = np.fft.fft2(E_ca)
D1 = np.fft.fftshift(D1)

I_ca = (np.abs(D1)/(lamda*R))**2

f1 = plt.figure(1)
plt.imshow(I_ca)


f2 = plt.figure(2)
plt.imshow(E_ca)

# The circular aperture w/ radius == 25 um
E_ca_sm = x**2+y**2 < (rds/2)**2

D1 = np.fft.fft2(E_ca_sm)
D1 = np.fft.fftshift(D1)

I_ca_sm = (np.abs(D1)/(lamda*R))**2

f3 = plt.figure(3)
plt.imshow(I_ca_sm)


f4 = plt.figure(4)
plt.imshow(E_ca_sm)

# The Chinese character "Zhong"
M1 = (np.abs(1*x) < rds) & (np.abs(2*y) < rds)
M2 = (np.abs(1.5*x) < rds) & (np.abs(3*y) < rds)
M3 = (np.abs(5*x) < rds) & (np.abs(1*y) < rds)

E_zh = M2 ^ M1 | M3

D1 = np.fft.fft2(E_zh)
D1 = np.fft.fftshift(D1)

I_zh = (np.abs(D1)/(lamda*R))**2

f5 = plt.figure(5)
plt.imshow(I_zh)


f6 = plt.figure(6)
plt.imshow(E_zh)


plt.show()