import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm

betas=[float(x)/1000 for x in range(1,11)]

x={}
y={}
meanx={}
meany={}
stdx={}
stdy={}
for i in betas:
	x[str(i)]=[]
	y[str(i)]=[]
	for j in range(1,10):
		if j==1:
			filename="Data/gameBeta"+str(i)+"Prob1.dat"
			print "loading "+ filename
			time, A, B=np.loadtxt(filename, 
				delimiter='\t', unpack=True)
			x[str(i)].append(A)
			y[str(i)].append(B)
		else:
			try:
				filename="Data/gameBeta"+str(i)+"Prob1.dat("+str(j)+')'
				print "loading "+ filename
				time, A, B=np.loadtxt(filename, 
					delimiter='\t', unpack=True)
				x[str(i)].append(A)
				y[str(i)].append(B)
			except:
				print "no such file\n"
	meanx[str(i)]=np.mean(x[str(i)], axis=0)
	meany[str(i)]=np.mean(y[str(i)], axis=0)
	stdx[str(i)]=np.std(x[str(i)], axis=0)
	stdy[str(i)]=np.std(x[str(i)], axis=0)
	

last=[]
max=[]
lasterror=[]
maxtime=[]
for i in betas:
	last.append(meanx[str(i)][-1])
	lasterror.append(stdx[str(i)][-1])
	max.append(meanx[str(i)].max())
	maxtime.append(meanx[str(i)].tolist().index(max[-1]))
	print maxtime
	figure=plt.figure()
	#fit=np.polyfit(np.log(time[1430:]), meanx[str(i)][1430:],1) Sistemare questa riga per fare il fil
	#fit_fn=np.poly1d(fit)
	plt.errorbar(range(len(meanx[str(i)])), meanx[str(i)], yerr=stdx[str(i)],alpha=0.5, label="mean NDW")
	#plt.plot(time[1430:], np.exp(fit_fn(time[1430:])), label="estimated value")
	plt.show()


plt.plot(betas,max,fmt='none', color='r', label='the last ndw')
#fit = np.polyfit(betas,last,1)
#fit_fn = np.poly1d(fit) 
#plt.plot(betas, fit_fn(betas), label="estimated value")
plt.xlabel('Beta')
plt.ylabel('Number of different words')
plt.legend()
plt.show()

