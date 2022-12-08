import  numpy as np
import matplotlib.pyplot as plt
import pandas as pd
numpyArray=np.linspace(0,10,20)#0 10 arasında 20 tane sayı
numpyArray2=numpyArray**3
myFigure=plt.figure()
figureAxes=myFigure.add_axes([0.1,0.1,0.9,0.9])
figureAxes.plot(numpyArray,numpyArray2,"g")
figureAxes.set_xlabel("X axis")
figureAxes.set_ylabel("Y axis")
figureAxes.set_title("Title")
#plt.show()
figure2=plt.figure()
eksen1=figure2.add_axes([0.1,0.1,0.7,0.7])
eksen2=figure2.add_axes([0.2,0.4,0.3,0.3])#burdaki değerler konum uzunluk ve genişlik verilerin içerir
eksen1.plot(numpyArray,numpyArray2,"g")
eksen1.set_xlabel("X Ekseni")
eksen1.set_ylabel("Y ekseni")
eksen1.set_title("Main Title")

eksen2.plot(numpyArray2,numpyArray,"b")
eksen2.set_xlabel("X Ekseni")
eksen2.set_ylabel("Y ekseni")
eksen2.set_title("Litle Title")
plt.show()







