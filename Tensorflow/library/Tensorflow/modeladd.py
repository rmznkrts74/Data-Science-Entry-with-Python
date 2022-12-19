import tensorflow as tf
import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
dataFrame=pd.read_excel("bisiklet_fiyatlari.xlsx")

##########################################################################
### veriyi test/train olarak ikiye ayırmak
#y=wx+b
#y->label
y=dataFrame["Fiyat"].values

x=dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=15)


####SCALING######## boyutu ayarlamak burda x ler 0 ile 1 arasındaki değerlere dö
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train=scaler.transform(x_train)
x_test=scaler.transform(x_test)

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
testPredict=model.predict(x_test)
#print(testPredict)
predictFrame=pd.DataFrame(y_test,columns=["Real Y"])
testPredict=pd.Series(testPredict.reshape(330))
#concat
predictFrame=pd.concat([predictFrame,testPredict],axis=1)
predictFrame.columns=["Real Y","Predict Y"]
#print(predictFrame)
#sbn.scatterplot(x="Real Y",y="Predict Y",data=predictFrame)
#plt.show()
from sklearn.metrics import mean_absolute_error,mean_squared_error
failNum=mean_absolute_error(predictFrame["Real Y"],predictFrame["Predict Y"])
otherNum=mean_squared_error(predictFrame["Real Y"],predictFrame["Predict Y"])
newCycle=[[1750,1751]]#yeni veriyle deneme
newCycle=scaler.transform(newCycle)
tryPredict=model.predict(newCycle)
#print(tryPredict)
from tensorflow.keras.models import load_model
model.save("cycle.h5")
lastcallmodel=load_model("cycle.h5")