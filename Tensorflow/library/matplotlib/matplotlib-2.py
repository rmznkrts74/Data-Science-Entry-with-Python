import matplotlib.pyplot as plt
import numpy as np

numpyArray=np.linspace(0,10,20)#0 10 arasında 20 tane sayı
numpyArray2=numpyArray**3
plt.plot(numpyArray,numpyArray2,"b*-")
#plt.show()

#yanyana iki tablo
plt.subplot(1,2,1)
plt.plot(numpyArray,numpyArray2,"r*-")
plt.subplot(1,2,2)
plt.plot(numpyArray2,numpyArray,"g*-")
#plt.show()

#newFıgure

myFigure=plt.figure()
figureAxes=myFigure.add_axes([0.2,0.2,0.9,0.9])
figureAxes.plot(numpyArray,numpyArray2,"g")
figureAxes.set_xlabel("X axis")
figureAxes.set_ylabel("Y axis")
figureAxes.set_title("Title")
plt.show()