import tensorflow as tf
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
dataFrame=pd.read_excel("bisiklet_fiyatlari.xlsx")
#print(dataFrame.head())
#sbn.pairplot(dataFrame)
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

####SCALING######## boyutu ayarlamak burda x ler 0 ile 1 arasındaki değerlere dö
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)
#print(x_train)#train elemanlarını döndürür
#print(x_train.shape)##train veri sayısını döndürür
model =Sequential()
#kaç hidden layer istiyorsak o kadar yazarız
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(4, activation="relu"))
model.add(Dense(1))#1 noron
model.compile(optimizer="rmsprop",loss="mse")#algoritmalar
model.fit(x_train,y_train,epochs=250)
loss=model.history.history["loss"]
trainloss=model.evaluate(x_train,y_train,verbose=0)
testloss=model.evaluate(x_test,y_test,verbose=0)
sbn.lineplot(x=range(len(loss)),y=loss)
print(testloss,trainloss)#son loss değeriini yazdırır loss değeri ne kadar düşükse o kadar verimli
#testloss ve trainloss birbirine ne kadar yakınsa o kadar verimli çalısmıstır.
plt.show()
