import pandas as pd
import  numpy as np
salaryDict={"Departman":["Software","Software","Marketing","Marketing","Law","Law"],
            "Name Of Worker":["Ahmet","Mehmet","Atil","Burak","Veli","Naz"],
            "Salary":[100,150,200,250,300,400]
            }
salaryDataFrame=pd.DataFrame(salaryDict)
grup=salaryDataFrame.groupby("Departman")
print(grup.count())#hangi departmanda kaç kişi çalişiyor gösterir
print(grup.mean())#departmanda ort. salary
print(grup.min())#min deger
print(grup.max())#max deger
print(grup.describe())##all info
print(salaryDataFrame)