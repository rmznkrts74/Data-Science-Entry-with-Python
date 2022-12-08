import pandas as pd
import numpy as np
salaryDict={"name":["Ahmet", "Mehmet","Atil","Burak"],
            "Departman":["Software","Marketing","Pazarlama","Software"],
            "Salary":[200,300,400,500]
            }
salaryDataFrame=pd.DataFrame(salaryDict)
x=salaryDataFrame["Departman"].unique()#departmanları tekrarsız bir sekilde getirir
print(x)
y=salaryDataFrame["Departman"].nunique()#departman sayısı
print(y)
z=salaryDataFrame["Departman"].value_counts()#deparmantlardaki eleman sayisi
print(z)
print(salaryDataFrame)
def brutToNet(salary):
    return salary*0.66
print(salaryDataFrame["Salary"].apply(brutToNet))
print(salaryDataFrame.isnull())#bos değer var mı yok mu
newData={"Character Class":["South Park", "South Park","Simpson","Simpson","Simpson"],
         "Names":["Cartman","Kenny","Homer","Bart","Bart"],
         "Age":[9,10,50,20,10]
         }

karakterDataFrame=pd.DataFrame(newData)
print(karakterDataFrame)
print(karakterDataFrame.pivot_table(values="Age",index=["Character Class","Names"],aggfunc=np.sum))
##aynı isimden iki tane varsa default olarak ortalamasını yazdırır ama aggfunc ile toplamını yazdırabiliriz
