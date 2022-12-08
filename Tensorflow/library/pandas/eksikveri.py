import pandas as pd
import numpy as np

dict1={"Istanbul":[30,20,np.nan],"Ankara":[20,np.nan,25],"Izmir":[40,39,38]}
weatherDataFrame=pd.DataFrame(dict1)
#print(weatherDataFrame)
#print(weatherDataFrame.dropna())#nan içeren satırları siler
#print(weatherDataFrame.dropna(axis=1))#0 da satırlar 1 de colonlar nan olmayan kolonları getirir
newDict={"Istanbul":[30,20,np.nan],"Ankara":[20,np.nan,25],"Izmir":[40,39,38],"Antalya":[45,np.nan,np.nan]}
newDataFrame=pd.DataFrame(newDict)
print(newDataFrame)
print(newDataFrame.dropna(axis=1,thresh=2))#2 ve daha fazla nan içeren kolonları siler
print(newDataFrame.fillna(20))#boş olanlara 20 yazdırır