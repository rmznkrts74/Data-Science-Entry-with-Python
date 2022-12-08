import matplotlib.pyplot as plt
import numpy as np
numpyArray=np.linspace(0,10,20)#0 10 arasında 20 tane sayı
numpyArray2=numpyArray**3
(myFigure,myEksenler)=plt.subplots(nrows=1,ncols=2)#kaç satır ve kolon olacagı döndürülür.
print(type(myEksenler))
#myEksenler.plot(numpyArray,numpyArray2,"r")

for eksen in myEksenler:
    eksen.plot(numpyArray,numpyArray2,"g")
    eksen.set_xlabel("X ekseni")
    eksen.set_ylabel("Y ekseni")
plt.tight_layout()#aralarındaki mesafe
plt.show()