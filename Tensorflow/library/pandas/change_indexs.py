import pandas as pd
import numpy as np
data=np.random.randn(4,3)#matrix oluşur
dataFrame=pd.DataFrame(data)##exceldeymiş gibi bir çıktı verir indexler yazılır
newDataFrame=pd.DataFrame(data,index=["Ali","Veli","Mehmet","Dark"],columns=["Salary","Age","Hour"])
#newDataFrame=newDataFrame.reset_index()##index kolonu olustuturur
newIndexList=["Al","Vel","Meh","Dar"]
newDataFrame["New Index"] = newIndexList
print(newDataFrame)
newDataFrame.set_index("New Index",inplace=True)#index kolonunu değiştirir
print(newDataFrame)
print(newDataFrame.loc["Al"])
