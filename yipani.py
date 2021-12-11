import math
import random
import matplotlib.pyplot as plt
from matplotlib import animation

PI=3.141592653589793238462643383
N=100000
x0=[]
y0=[]
x=[]
y=[]
xc1=-9
xc2=-9
sigma=0.5
omega=1
nl=30
lmda=20/nl
k=2*PI/lmda
yc1=2*lmda
yc2=-2*lmda

fig, a=plt.subplots()

for i in range(N+1):
	x0.append(10*(1-2*random.random()))
	y0.append(10*(1-2*random.random()))
	x.append(0)
	y.append(0)

def norm(x,y):
	return(math.sqrt(x**2+y**2))

def gamma(x,y,t):
	return(1+2*PI*sigma*math.sin(k*norm(x,y)-omega*t)/(k*norm(x,y)))

def run(frame):
	plt.clf()
	for i in range(N+1):
		x[i]=(x0[i]-xc1)*gamma(x0[i]-xc1,y0[i]-yc1,frame)+(x0[i]-xc2)*gamma(x0[i]-xc2,y0[i]-yc2,frame)+x0[i]
		y[i]=(y0[i]-yc1)*gamma(x0[i]-xc1,y0[i]-yc1,frame)+(y0[i]-yc2)*gamma(x0[i]-xc2,y0[i]-yc2,frame)+y0[i]
	plt.scatter(x,y,s=1,color='r')
	ax=plt.gca()
	ax.set_aspect(1)
	plt.xlim([-9,9])
	plt.ylim([-9,9])
	ax.set_facecolor('xkcd:black')
    
ani=animation.FuncAnimation(fig,run,interval=1)
writervideo = animation.FFMpegWriter(fps=10)
ani.save('yipani.mp4', writer=writervideo)
plt.show()
