import pylab as plt
import numpy as np

R = 1
lamda = 500E-9
d = 50E-6
side = np.linspace(-0.01*np.pi, 0.01*np.pi, 200)
x, y = np.meshgrid(side, side)

side_2 = np.linspace(-5*d, 5*d, 200)
#side_2 = np.linspace(0.1,0.1,200)
x_0, y_0 = np.meshgrid(side_2, side_2)

E_field = x_0**2+y_0**2 < (d/2)**2
E_field.astype(float)



D1 = np.fft.fft2(E_field)

D2=D1
D2 = np.fft.fftshift(D1)
#D2=E_field
abs_image = np.abs(D2)
#plt.imshow(abs_image)
#plt.show()


#intensity = abs(E_field)**2

#print intensity[100]

f1 = plt.figure(1)
plt.pcolormesh(x, y, abs_image)
f1.show()

#f1 = plt.figure(1)
#plt.pcolormesh(x, y, intensity)
#f1.show()

#f2 = plt.figure(2)
#plt.gray()
#plt.pcolormesh(x, y, intensity)
#f2.show()

#f3 = plt.figure(3)
#plt.jet()
#plt.pcolormesh(x, y, np.sqrt(intensity))
#f3.show()



plt.show()