import pandas as pd
import numpy as np
dict1={"name":["Ahmet","Mehmet","Atil","Burak"],
       "Spor":["Run","Swim","Basket","Run"]
       ,"Kalori":[100,200,300,400]
       }
dict2={"name":["Osman","Levent","Zeynep","Naz"],
       "Spor":["Run","Swim","Basket","Run"]
       ,"Kalori":[100,200,300,400]
       }
dict3={"name":["Ayse","Elif","Veli","Ali"],
       "Spor":["Run","Swim","Basket","Run"]
       ,"Kalori":[100,200,300,400]
       }
dataFrame1=pd.DataFrame(dict1,index=[0,1,2,3])
dataFrame2=pd.DataFrame(dict1,index=[4,5,6,7])
dataFrame3=pd.DataFrame(dict1,index=[8,9,10,11])
#concatenation(Birlestirme)
print(pd.concat([dataFrame1,dataFrame2,dataFrame3],axis=0))