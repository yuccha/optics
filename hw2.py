from visual import *
from visual.graph import *
import copy
import math
print '\n------ Program starts ------'
#------matrix multiply function------#
# This function can only be used in the multiplication between two nxn matrices
# default order is 2!
def multpy (m1, m2, order=2):
	opmat = [[0,0],[0,0]]
	for i in range(0,order):
		for j in range(0,order):
			for k in range(0,order):
				opmat[i][j] += m1[i][k]*m2[k][j]
	return opmat

#------parameters of this system------#
cycle = 300	#	number of cycles
R1 = 40.0 #cm	the radius of curvature of mirror 1
R2 = 50.0 #cm	the radius of curvature of mirror 2
f = 9 #cm		the focal length of the thin lens
l = 10.0 #cm	the distance between mirror 1 and thin lens
ll = 50.0 #cm	the distance between mirror 2 and thin lens

D_l = [[1.0,l],[0.0,1.0]]			#ABCD matrix of translation from mirror 1 to lens
D_ll = [[1.0,ll],[0.0,1.0]]			#ABCD matrix of translation from mirror 2 to lens
M_f = [[1.0,0.0],[-1.0/f,1.0]]		#ABCD matrix of thin lens f
M_R1 = [[1.0,0.0],[-2.0/R1,1.0]]	#ABCD matrix of mirror 1
M_R2 = [[1.0,0.0],[-2.0/R2,1.0]]	#ABCD matrix of mirror 2

#------ABCD matrix of one cycle------#
mtrx =  multpy(M_R1, multpy(D_l, multpy(M_f, multpy(D_ll, multpy(M_R2, multpy(D_ll, multpy(M_f, D_l)))))))
trace = (mtrx[0][0] + mtrx[1][1])/2


print "\n|(A+D)/2| = %.2f" % math.fabs(trace)
#print '\n|(A+D)/2| = ' + str(math.fabs(trace))
if trace > 1 or trace <-1:
	print 'As a result, this system is not stable!'
else:
	print 'As a result, this system is stable!'
#print mtrx			# Print out the matrix
#print trace		# Print out the value of A+D

#------graph of r v.s cycle------#
print '\n*** r as a funtion of cycle is demonstrated ***'
g1 = gdisplay(xtitle = 'number of cycles', ytitle = 'r (Distance between the ray and the optics axis)', xmax=303, xmin=0, ymax=0.6, ymin=-0.6)
fig = gcurve(color = color.cyan)
ini = [[0.5,0.0],[0.0,0.0]]		# generate a 2x2 [[a,0],[b,0]] matrix to represent a 2x1 matrx [a,b]
mat_ini = multpy(mtrx, ini)		# ray vector after a cycle
for idx in range (0,cycle):		# ray vector after 300 cycles!
	rate(100)
	mat_ini = copy.deepcopy(multpy(mtrx,mat_ini))
	posi = vector(idx,mat_ini[0][0])						# r v.s cycle
	fig.plot(pos = posi)
print '\nThis shows a periodic function r of cycle.\n\'r\' is bounded, which shows that this system is stable!'
print 'The ray ended at (r, r\') = (%.3f, %.3f) after %i cycles' %(mat_ini[0][0], mat_ini[1][0], cycle)

print '\n------ Program ends here ------'

# add a new comment to test the github!
