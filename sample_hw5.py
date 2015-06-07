import pylab as plt
import numpy as np
import copy

R = 1
lamda = 500E-9
scn = 1E-6
tms = 400
rds_tm = 25
#rds = scn*rds_tm
rds = 25E-6

#----- Diffraction diagram of circular aperture (by impulse response method.) -----#
side = np.linspace(-0.05*np.pi, 0.05*np.pi, 200)
x,y = np.meshgrid(side, side)
x0,y0 = np.meshgrid(np.linspace(0,0,200),np.linspace(0,0,200))	# used to initialize E_ca
E_ca = x0+y0*1j

for xid in np.arange(-30*scn, 30*scn, scn):
	for yid in np.arange(-30*scn, 30*scn, scn):
		if np.sqrt(xid**2+yid**2) < rds:
			E_ca += np.exp(1j*((x-xid)**2+(y-yid)**2)/(R*lamda))

I_ca = (np.abs(E_ca)/(lamda*R))**2

I_ca2 = copy.deepcopy(I_ca)

r_crit = 1.22*lamda*R/(2*rds)
E_c = (x**2+y**2 < 1.1*r_crit**2) & (x**2+y**2 > 0.8*r_crit**2)

f1 = plt.figure(1)
plt.imshow(I_ca)
#plt.pcolormesh(x,y,I_ca)

#--- fig 2 shows the diffraction diagram with a reddish-brown ring, which denotes the Rayleigh criteria in theory ---# 
f2 = plt.figure(2)
plt.imshow(I_ca2)
#plt.pcolormesh(x,y,I_ca2)

I_c = (np.abs(E_c)/(lamda*R))**2
I_ca2 += (I_c*10E19)	# multiply with the highest peak so that we can make this ring standout.

#----- Diffraction matrix of circular aperture, with radius = 50 um (by Fourier Transform method.) -----#
side = np.linspace(-scn*tms,scn*tms,tms/2)
x1,y1 = np.meshgrid(side, side)
E_cf = x1**2+y1**2 < rds**2

D1 = np.fft.fft2(E_cf)
D1 = np.fft.fftshift(D1)

I_cf = (np.abs(D1)/(lamda*R))**2

f3 = plt.figure(3)
plt.imshow(I_cf)

#----- Smaller circular aperture, radius = 25 um (by Fourier Transform) -----#
E_cf_sm = x1**2+y1**2 < (rds/2)**2

D1 = np.fft.fft2(E_cf_sm)
D1 = np.fft.fftshift(D1)

I_cf_sm = (np.abs(D1)/(lamda*R))**2

f4 = plt.figure(4)
plt.imshow(I_cf_sm)

#----- Diffraction diagram of the Chinese character "Zhong" -----#
M1 = (np.abs(0.7*x1) < rds) & (np.abs(1.4*y1) < rds)
M2 = (np.abs(1.05*x1) < rds) & (np.abs(2.1*y1) < rds)
M3 = (np.abs(3.5*x1) < rds) & (np.abs(0.7*y1) < rds)

E_zh = M2 ^ M1 | M3

D1 = np.fft.fft2(E_zh)
D1 = np.fft.fftshift(D1)

I_zh = (np.abs(D1)/(lamda*R))**2

f5 = plt.figure(5)
plt.imshow(I_zh)

#--- fig 6 shows the shape of the aperture ---#
f6 = plt.figure(6)
plt.imshow(E_zh)

plt.show()