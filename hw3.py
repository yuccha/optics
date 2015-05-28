from visual import *
from visual.graph import *
import math

## ---- Initializing ---- ##
# u"\u03BB" is lamda!!
lb_min = 495	# nm
lb_max = 505	# nm
label_pos = 507
strg = 'Wavelength (' + u"\u03BB" + ')'	# strg = "Wavelength (lamda)"
g1 = gdisplay(xtitle = strg, ytitle = 'Normalized Spectrum (a.u.)', xmax=lb_max, xmin=lb_min, ymax=1.05, ymin=0.0)
f4 = gdots(color = color.yellow, size = 4)
f1 = gcurve(color = color.cyan)
f2 = gcurve(color = color.red)
f3 = gcurve(color = color.green)
label(display=g1.display, pos=(label_pos, 1.0), text='Cyan curve: Etalon 1', opacity = 0, linecolor = scene.background, color = color.cyan, xoffset = -1, line = 0)
label(display=g1.display, pos=(label_pos, 0.9), text='Red curve: Etalon 2', opacity = 0, linecolor = scene.background, color = color.red, xoffset = -1, line = 0)
label(display=g1.display, pos=(label_pos, 0.8), text='Green curve: Etalon 3', opacity = 0, linecolor = scene.background, color = color.green, xoffset = -1, line = 0)
label(display=g1.display, pos=(label_pos, 0.7), text='Yellow dots: Light source', opacity = 0, linecolor = scene.background, color = color.yellow, xoffset = -1, line = 0)

f_list = [f1, f2, f3]

## ---- Define functions ---- ##
def spec(lbda, a=1.0, b=0.1, c=0.1, lb_a=502, lb_ae=0.4, lb_c=501, lb_ce=0.2, lb_b=497, gamma=0.6):
	return a*math.exp(-((lbda-lb_a)/lb_ae)**2)+c*math.exp(-((lbda-lb_c)/lb_ce)**2)+b*(gamma/2)/((lbda-lb_b)**2+(gamma/2)**2)
## spec(lamda) is the spectrum of light source

def trans(lbda, length, R, n=1.0, theta=0.0):
	delta = 4.0*math.pi*n*length*math.cos(theta)/lbda
	return (1.0-R)**2/((1.0-R)**2+4.0*R*(math.sin(delta/2))**2)
## trans (lamda, length, R), is the transmittance of Fabry-Perot etalon

def find_pk(leng, R, lb_min=495, lb_max=505, dtt = 0.01):
	intensity = 0
	for lmbda in arange (lb_min, lb_max, dtt):
		intensity += spec(lmbda)*trans(lmbda, leng, R)
	return intensity
## find_pk(length, R) is the ourput intensity for a given length

## ---- Second initializing ---- ##
R_list = [0.8, 0.99, 0.99]				# R for case 1, 2, 3 respectively
m_list = [20.0, 40.0, 20.0]				# m for case 1, 2, 3 respectively
length_st = 9900.0
length_ed = 10100.0
# thickness start from 9900 to 10100, for case 2, simply multiply by two!
dt = 0.1 			# Increasing the thickness by 0.1 after each measurement
dtt = 0.01 			# Increasing the wavelength by 0.01 while measuring
iterator = 0 		# an iterator, used to cut down on the dots of light source in the graph

## ---- Calculating starts ---- ##
for leng in arange(length_st, length_ed, dt):
	rate(10**10)
	pk_insty = [0.0,0.0,0.0]
	for i_case in range(0,3):
		in_leng = leng
		maxi_len = 502*20
		# Maximum occurs in 502 nm
		if i_case == 1:
			in_leng *= 2
			maxi_len *= 2
		# For case 2, the thickness is twice of those in case 1 and 3.
		pk_insty[i_case] = find_pk(in_leng, R_list[i_case])/find_pk(maxi_len, R_list[i_case])
		# normalizing the spectrum by deviding intensity(502), the maximum peak value.
		f_list[i_case].plot(pos = (leng/m_list[0], pk_insty[i_case]))
		# Plot case1~3
	if iterator % 25 == 0:
		f4.plot(pos = (leng/20, spec(leng/20)))
	# plot the light source graph only when iterator % 25 == 0, in order to cut down on the numbers of dots.
	iterator += 1

print 'Etalon III, with with R=0.99 and thickness t scans from 9900 nm to 10100 nm, is a better Fabry-Perot etalon in measuring the spectrum'
print 'end'




