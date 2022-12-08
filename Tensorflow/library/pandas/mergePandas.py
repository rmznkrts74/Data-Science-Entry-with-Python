##MERGE
import pandas as pd
import numpy as np
mergedict1={"name":["Ahmet","Mehmet","Atil","Burak"],
       "Spor":["Run","Swim","Basket","Run"]
       }
mergedict2={"name":["Ahmet","Mehmet","Atil","Burak"],
       "Kalori":[100,200,300,400]
       }

mergedataFrame1=pd.DataFrame(mergedict1)
mergedataFrame2=pd.DataFrame(mergedict2)
print(pd.merge(mergedataFrame1,mergedataFrame2,on="name"))#on ile hangi kolon ustunden ortak işlem yapılacığını belirleriz