import numpy as np
newArray=np.random.randint(1,100,20)
print(newArray>24)#24 ten buyuk olan tüm değerlei true olarka döndürür
sonucArray=newArray>24
print(newArray[sonucArray]) #değerleri yazdırır
lastArray=np.arange(0,24)
print(lastArray+lastArray)#arraydeki değerleri kendisiyle toplar
print(lastArray*lastArray)#arraydeki değerleri kendisiyle çarpar
print(lastArray-lastArray)#arraydeki değerleri kendisinden çıkarır
print(np.sqrt(lastArray))
print(np.max(lastArray))
print(np.min(lastArray))