import numpy as np
##index
newArray=np.arange(0,15)
#print(newArray[5])#listeyle aynı
#print(newArray[3:8])#listeyle aynı
#newArray[3:8]=-5##aralıktaki elemanları -5 e eşitler
#print(newArray)
otherArray=np.arange(0,24)
slicingDizisi=otherArray[4:9]
#print(slicingDizisi)
slicingDizisi[:]=700#butun elemanları 700 e eşitler
#print(otherArray)#ust satırdaki islem yuzunden burda da aynı aralıktaki değerler 700 değerin alıyor
##yukardaki olay olmasın diye bunları yapmalıyız
newArraycopy=newArray.copy()
slicingDizisi2=newArraycopy[3:8]
slicingDizisi2[:]=700
print(slicingDizisi2)
print(newArray)
print(newArraycopy)
