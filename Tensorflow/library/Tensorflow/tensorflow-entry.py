import tensorflow 
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
dataFrame=pd.read_excel("bisiklet_fiyatlari.xlsx")
#print(dataFrame.head())
sbn.pairplot(dataFrame)
plt.show()