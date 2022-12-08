import  numpy as np
import pandas as pd
## data frame #serilerin yanyana gelmesiyle olusmuş excel tablosu gibi bir yapı
data=np.random.randn(4,3)#matrix oluşur
dataFrame=pd.DataFrame(data)##exceldeymiş gibi bir çıktı verir indexler yazılır
#print(dataFrame)#tüm tablo yazdırılır
#print(dataFrame[0])#ilk kolon yazdırılır
#print(dataFrame[0][1])#ilk kolon 1.index
newDataFrame=pd.DataFrame(data,index=["Ali","Veli","Mehmet","Dark"],columns=["Salary","Age","Hour"])
print(newDataFrame)
print(newDataFrame["Age"])
print(newDataFrame[["Salary","Age"]])
print(newDataFrame.loc["Veli"])##for look line by line
print(newDataFrame.iloc[1])#index bazlı olarak çagırır