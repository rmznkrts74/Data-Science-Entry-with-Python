import numpy as np
import pandas as pd
#string kullanmak
x=pd.Series(data=["Ali","Veli","Mehmet","Dark"],index=[1,2,3,4])
#print(x)
result1=pd.Series(data=[90,80,100,20],index=["Ali","Veli","Mehmet","Dark"])
#print(result1)
result2=pd.Series(data=[20,10,8,15],index=["Ali","Veli","Mehmet","Dark"])
#print(result2)
lastResult=result1+result2#her indexe karsılık gelen değerleri toplaar ve toplamı gösterilir
#print(lastResult)
