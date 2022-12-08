import numpy as np

##numpy dizi methodları
normalArray=np.arange(25)
randomArray=(np.random.randint(0,100,20))
#print(normalArray ,"\n", randomArray)
print(normalArray.reshape(5,5))##burda arrayin boyutu önemli girilen sayıların carpımı kadar olmalı
x=normalArray.max()
y=randomArray.min()
a=randomArray.argmax()#maxın indexini verir argmin min için kullanılır
print(x,"\n",y,"\n",a)
reshapeArray=normalArray.reshape(5,5)
print(normalArray.shape)#normal dizinin hangi skilde oldugunu gösterir
print(reshapeArray.shape)