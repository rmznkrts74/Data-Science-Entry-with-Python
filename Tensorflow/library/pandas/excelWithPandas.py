import pandas as pd
dataFrame = pd.read_excel('salary.xlsx')
print(dataFrame)
print(dataFrame.dropna())#bos deger olan satırları siler
doluDeger=dataFrame.dropna()
print(doluDeger)
doluDeger.to_excel('newSalary.xlsx')
