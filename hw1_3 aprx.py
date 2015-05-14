from visual import *
from visual.graph import *
import math

n1 = 1.5
g = 2 # 1/mm
beta = n1
g1 = gdisplay()

f1 = gcurve(color = color.cyan)
f2 = gcurve(color = color.red)
f3 = gcurve(color = color.green)

f_list = [f1, f2, f3]
#ini_pos = vector(0.0,0.0,0.0)
pos_list = [vector(0.0,0.0,0.0), vector(0.0,0.0,0.0), vector(0.0,0.0,0.0)]
#ini_v = vector (0.1, 0.7, 0.8)
velo_list = [vector (0.1, 0.7, 0.8), vector (0.1, 0.7, 0.8), vector (0.1, 0.7, 0.8)]
numlis = [0, 0, 0]
period = [0, 0, 0]
dt = 0.0001

for x in arange(0, 8.05, dt):
	acce = [0, 0, 0]
	acce[0] = -2*(n1**2)*g*((math.cosh(g*pos_list[0].y))**(-2))*math.tanh(g*pos_list[0].y)/(2*beta**2)
	acce[1] = -g*math.tanh(g*pos_list[1].y)
	costheta = velo_list[2].x/((velo_list[2].x**2+velo_list[2].y**2)**(0.5))
	acce[2] = -g*math.tanh(g*pos_list[2].y)/(costheta**2)

	for i in range(0, 3):
		velo_list[i].y += acce[i]*dt
		pos_list[i].x += velo_list[i].x*dt
		pos_list[i].y += (velo_list[i].y*dt + 0.5*acce[i]*dt**2)
		f_list[i].plot(pos = pos_list[i])
		if period [i] == 0 and numlis[i] < 0 and pos_list[i].y > 0:
			period[i] = pos_list[i].x
		numlis[i] = pos_list[i].y

#	velo_list[0].y += acce[0]*dt
#	velo_list[1].y += acce[1]*dt
#	velo_list[2].y += acce[2]*dt
#	pos_list[0].x += velo_list[0].x*dt
#	pos_list[1].x += velo_list[1].x*dt
#	pos_list[2].x += velo_list[2].x*dt
#	pos_list[0].y += (velo_list[0].y*dt + 0.5*acce[0]*dt**2)
#	pos_list[1].y += (velo_list[1].y*dt + 0.5*acce[1]*dt**2)
#	pos_list[2].y += (velo_list[2].y*dt + 0.5*acce[2]*dt**2)
#	f1.plot(pos = pos_list[0])
#	f2.plot(pos = pos_list[1])
#	f3.plot(pos = pos_list[2])
#print pos_list[0], pos_list[1], pos_list[2]

stri = 'The Period is:\n'
str_list = ['Case I (Cyan):	', 'Case II (Red):	', 'Case III (Green):	']
for i in range(0, 3):
	stri += (str_list[i] + str(period[i]) + '\n')
label(display=g1.display, pos=(0.1,-0.3), text=stri, opacity = 0, linecolor = scene.background)
#print period[0], period[1], period[2]
#print stri
print 'end'