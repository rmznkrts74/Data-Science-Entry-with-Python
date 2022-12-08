import numpy as np
import pandas as pd
# data Frame
data=np.random.randn(4,3)#matrix oluşur
dataFrame=pd.DataFrame(data)##exceldeymiş gibi bir çıktı verir indexler yazılır
newDataFrame=pd.DataFrame(data,index=["Ali","Veli","Mehmet","Dark"],columns=["Salary","Age","Hour"])
## yeni column eklemek için
newDataFrame["Other"]=newDataFrame["Age"]*2
##column silmek için
#print(newDataFrame.drop("Other",axis=1))
##row silmek için
#print(newDataFrame.drop("Veli"))
#print(newDataFrame.drop("Other", axis=1,inplace=True))#inplace ile matrix burdaki son halini korur
print(newDataFrame)
print(newDataFrame.loc["Ali"]["Salary"])#altakiyle aynı
print(newDataFrame.loc["Ali","Salary"])
print(newDataFrame<0)#filtreleme
