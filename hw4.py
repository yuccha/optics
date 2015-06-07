from visual import *
from visual.graph import *
import math
import csv

lmda_beg = 490.0
lmda_end = 510.0
dlmda = 0.1
c = 3E17
dlta_end = 5000000.0
d_dlta = 50
strg = 'Wavelength (' + u"\u03BB" + ')'	# strg = "Wavelength (lamda)"

g1 = gdisplay(xtitle = strg, ytitle = 'Normalized Spectrum (a.u.)', xmax=lmda_end, xmin=lmda_beg, ymax=1.05, ymin=0.0)
f1 = gcurve(color = color.cyan)

It = dict()
for key, val in csv.reader(open("output.csv")):
	It[int(key)] = float(val)

Itt = 0.5*It[0]

pk_max = 0.0

max_lmda = 502.0
for dlta in arange(0, dlta_end, d_dlta):
	gamma = (It[dlta]-Itt)/Itt
	pk_max += gamma*math.cos(2.0*math.pi*dlta/max_lmda)*d_dlta


for lmda in arange(lmda_beg, lmda_end, dlmda):
	rate (1000000)
	Is = 0
	for dlta in arange(0, dlta_end, d_dlta):
		gamma = (It[dlta]-Itt)/Itt
		Is += gamma*math.cos(2.0*math.pi*dlta/lmda)*d_dlta
	Is /= pk_max
	f1.plot(pos = (lmda, Is))
