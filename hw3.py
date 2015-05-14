from visual import *
from visual.graph import *
import math

# for case I first: I ll plot the ordinary etalon diagram.

lb_min = 495	# nm
lb_max = 505	# nm
g1 = gdisplay(xmax=505, xmin=495, ymax=1.0, ymin=0.0)
f4 = gcurve(color = color.yellow)
f1 = gcurve(color = color.cyan)
f2 = gcurve(color = color.red)
f3 = gcurve(color = color.green)

f_list = [f1, f2, f3]

def spec(lbda, a=1.0, b=0.1, c=0.1, lb_a=502, lb_ae=0.4, lb_c=501, lb_ce=0.2, lb_b=497, gamma=0.6):
	return a*math.exp(-((lbda-lb_a)/lb_ae)**2)+c*math.exp(-((lbda-lb_c)/lb_ce)**2)+b*(gamma/2)/((lbda-lb_b)**2+(gamma/2)**2)

def trans(lbda, length, R, n=1.0, theta=0.0):
	delta = 4.0*math.pi*n*length*math.cos(theta)/lbda
	return (1.0-R)**2/((1.0-R)**2+4.0*R*(math.sin(delta/2))**2)

def find_pk(leng, R, lb_min=495, lb_max=505, dtt = 0.01):
	intensity = 0
	for lmbda in arange (lb_min, lb_max, dtt):
		intensity += spec(lmbda)*trans(lmbda, leng, R)
	return intensity

# ---- start calculating ---- #
len_start = [9900.0, 19800.0, 9900.0]
len_end = [10100.0, 20200.0, 10100.0]
R_list = [0.8, 0.99, 0.99]
m_list = [20.0, 40.0, 20.0]
length_st = 9900.0
length_ed = 10100.0
#len_start = [9900.0, 9900.0, 9900.0]
#len_end = [10100.0, 10100.0, 10100.0]
#R_list = [0.9, 0.95, 0.99]
#m_list = [20.0, 20.0, 20.0]
dt = 0.1
dtt = 0.01
##

for leng in arange(length_st, length_ed, dt):
	rate(10**10)
	pk_insty = [0.0,0.0,0.0]
	for i_case in range(0,3):
		in_leng = leng
		maxi_len = 502*20
		if i_case == 1:
			in_leng *= 2
			maxi_len *= 2
		pk_insty[i_case] = find_pk(in_leng, R_list[i_case])/find_pk(maxi_len, R_list[i_case])		
#		for lmbda in arange (lb_min, lb_max, dtt):
#			if i_case == 1:
#				intensity[i_case] += spec(lmbda)*trans(lmbda, 2*leng, R_list[i_case])
#			else:
#				intensity[i_case] += spec(lmbda)*trans(lmbda, leng, R_list[i_case])
		f_list[i_case].plot(pos = (leng/m_list[0], pk_insty[i_case]))
	f4.plot(pos = (leng/20, spec(leng/20)))


#for i_case in range(0, 3):
#	for leng in arange(len_start[i_case], len_end[i_case], dt):
#		rate(10000)
#		intensity = 0
#		for lmbda in arange (lb_min, lb_max, dtt):
#			intensity += spec(lmbda)*trans(lmbda, leng, R_list[i_case])
#		if i_case == 0:
#			posi2 = vector(leng/20, spec(leng/20))
#			f4.plot(pos = posi2)
#		posi = vector(leng/m_list[i_case], intensity)
#		f_list[i_case].plot(pos = posi)
print 'end'




