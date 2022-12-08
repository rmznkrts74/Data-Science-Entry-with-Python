import matplotlib.pyplot as plt
import numpy as np
numpyArray1=np.linspace(0,10,20)
numpyArray2=numpyArray1**2
(myFigure,myEksen)=plt.subplots()
myEksen.plot(numpyArray1,numpyArray2,"g",linewidth=5.0,linestyle="--")#color=hexcode ile istenilen renkler yapılabilir linewidth kalınlığı ayarlar 
myEksen.plot(numpyArray2,numpyArray1,"b",linewidth=1.0,linestyle=":",marker="o",markerfacecolor="red")

#plt.show()

#scatter plot
plt.scatter(numpyArray1,numpyArray2)
plt.show()

#histogram
newDizi=np.random.randint(0,100,50)
plt.hist(newDizi)
plt.show()


##boxplot

plt.boxplot(newDizi*2)
plt.show()