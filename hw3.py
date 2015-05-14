from visual import *
from visual.graph import *
import math

# for case I first: I ll plot the ordinary etalon diagram.

lb_min = 495	# nm
lb_max = 505	# nm
#l = 9900*10**(-9)		# nm
#l = 10100*10**(-9)		# nm
#l = 19800*10**(-9)		# nm
#l = 20200*10**(-9)		# nm
#c = 3*10**8

#----
#fsr = c/(2*n*l*math.cos(theta))
#v_max = c/lb_min
#v_min = c/lb_max
#print 'Free spectrum range = %s' %(fsr)
#print 'Real spectrum range = %s' %(v_max-v_min)

#----

def spec(lbda, a=1.0, b=0.1, c=0.1, lb_a=502, lb_ae=0.4, lb_c=501, lb_ce=0.2, lb_b=497, gamma=0.6):
	return a*math.exp(-((lbda-lb_a)/lb_ae)**2)+c*math.exp(-((lbda-lb_c)/lb_ce)**2)+b*(gamma/2)/((lbda-lb_b)**2+(gamma/2)**2)

def trans(lbda, length, R, n=1.0, theta=0.0):
	delta = 4.0*math.pi*n*length*math.cos(theta)/lbda
	return (1.0-R)**2/((1.0-R)**2+4.0*R*(math.sin(delta/2))**2)

# ---- start calculating ---- #
len_start = [9900.0, 19800.0, 9900.0]
len_end = [10100.0, 20200.0, 10100.0]
R_list = [0.8, 0.99, 0.99]
dt = 0.001
##
for i_case in range(0, 3):
	intensity = 0
	for leng in arange(len_start[i_case], len_end[i_case], dt):
		for lmbda in arange (lb_min, lb_max, dt):
			intensity += spec(lmbda)*trans(lmbda, leng, R_list[i_case])
		# plot the intensity versus len/20 (=lambda!!)
		# need to add an array consisting the graph's color!




