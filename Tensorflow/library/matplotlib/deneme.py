import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import openpyxl #for read file
data=pd.read_excel("veri.xlsx")
data['Banka']=data["Banka"].astype('string')
data['Max']=data['Max'].asytpe('float')
data.head()
plt.figure(figsize=(12,6))
plt.plot(data.Banka,data.Max)
plt.show()