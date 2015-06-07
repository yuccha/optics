import numpy as np
import pylab as py
from scipy import misc, fftpack

n = 2**10
I = np.arange(1, n)
x = I - n / 2
y = n / 2 - I

R = 10

X = x[:, np.newaxis]
Y = y[np.newaxis, :]

M = X**2 + Y**2 < R**2
for ttt in M[516]:
	print ttt

#D1 = fftpack.fft2(M)
#D2 = fftpack.fftshift(D1)

abs_image = np.abs(D2)
py.imshow(abs_image)
py.show()