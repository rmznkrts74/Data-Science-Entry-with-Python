import tensorflow as tf
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
dataFrame=pd.read_excel("bisiklet_fiyatlari.xlsx")
#print(dataFrame.head())
sbn.pairplot(dataFrame)
#plt.show()

##########################################################################
### veriyi test/train olarak ikiye ayırmak
#y=wx+b
#y->label
y=dataFrame["Fiyat"].values
#x=feature
x=dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=15)
#print(x_train.shape)#train data sayısını verir
#print(x_test)#test verilerini yazdırır

####SCALING########
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)
#print(x_train)
