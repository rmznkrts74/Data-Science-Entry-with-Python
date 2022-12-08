import matplotlib.pyplot as plt
import numpy as np
numpyArray=np.linspace(0,10,20)#0 10 arasında 20 tane sayı
numpyArray2=numpyArray**3
newFigur=plt.figure(figsize=(6,6))#boyut ayarıve dpi ile kalitesi artırılıyor
newEksen=newFigur.add_axes([0.1,0.1,0.9,0.9])
newEksen.plot(numpyArray,numpyArray**3,"r",label="numpyDizisi**3")#label ne verisi oldugunu ekrana etiket olarka bastırır
newEksen.plot(numpyArray,numpyArray**2,"g",label="Numpy Dizisi**2")
newEksen.legend(loc=0)#etiketin olacagı yeri belirleyebiliyoruz
newFigur.savefig("myfirst.png",dpi=200)
plt.show()