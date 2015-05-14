from visual import *
from visual.graph import *
import math

n1 = 1.5
g = 2 
g1 = gdisplay()

fig = gcurve(color = color.cyan)

posi = vector(0.0,0.0,0.0)
velo = vector (0.1, 0.7, 0)							#initial velocity
pre_y = 0
pre_vy = 0
period = 0
lst_per = 0
dt = 0.0001
max_pos = vector(0.0,0.0,0.0)
peri_list = []

for x in arange(0, 8.05, dt):
	rate(10000)
	costheta = velo.x/((velo.x**2+velo.y**2)**(0.5))	#cosine
	acce = -g*math.tanh(g*posi.y)/(costheta**2)			#acceleration, just like the mechanics
	velo.y += acce*dt
	posi.x += velo.x*dt
	posi.y += velo.y*dt + 0.5*acce*dt**2
	fig.plot(pos = posi)
	if pre_y < 0 and posi.y > 0:
		period = posi.x - lst_per
		peri_list.append(period)
		lst_per = posi.x
	pre_y = posi.y
	if max_pos.x == 0 and pre_vy > 0 and velo.y < 0:
		max_pos = vector(posi)
	pre_vy = velo.y
peri_siz = 0
period = 0
for s in peri_list:
	period += s
	peri_siz += 1
period /= peri_siz

max_pos.x *= 1.2
max_pos.y *= -0.9


stri = 'Period: '
stri += str(period)
label(display=g1.display, pos=max_pos, text=stri, opacity = 0, linecolor = scene.background, height = 16)
print stri
print 'end'