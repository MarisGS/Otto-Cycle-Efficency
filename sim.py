def otto (gamma1, gamma2):

	import matplotlib.pyplot as plt
	from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,AutoMinorLocator)
	import numpy as np

	# piešķir vērtības siltumietilpību attiecībai Gamma, vienā un otrā scenārijā:

	#gamma1=1.3
	#gamma2=1.6

	# iniciē parametrus: 

	CR=np.zeros(29) +1
	CR2=np.zeros(29) +1

	CR[0]=1
	CR2[0]=1

	eta=np.zeros(29)
	eta2=np.zeros(29)


	# sāk aprēķinu ciklā:

	for ii in range(1,28):

        	eta[ii]= (1-1/CR[ii]**(gamma1-1))*100
       
        	eta2[ii]=(1-(1/CR2[ii]**(gamma2-1)))*100 
       
    
    
        	CR[ii+1]=CR[ii]+1
        	CR2[ii+1]=CR2[ii]+1

	#sagatavo un parāda diagrammu


	Gamma_str=str(round(gamma1,2))
	Gamma_str2=str(round(gamma2,2))

	label1=('$\gamma$='+Gamma_str)
	label2=('$\gamma$='+Gamma_str2)


	fig, ax = plt.subplots()
	ax.grid()
	ax.set_ylabel('Efficency, %')
	ax.set_xlabel('Ratio of compression')

	maxval=np.max([np.max(eta2)])
	#minval=np.min([np.min(T_cyl_a), np.min(T_cyl_b)])
	ylim_1=0
	ylim_2=maxval+10

	ax.set_xlim(0, 25)
	ax.set_ylim(ylim_1, ylim_2)
	#ax.xaxis.set_major_locator(MultipleLocator(1)) # distribute major ticks on x axis
	line, = ax.plot(CR,eta, label=label1)
	line2, = ax.plot(CR2,eta2, label=label2)

	ax.legend()
	plt.show()