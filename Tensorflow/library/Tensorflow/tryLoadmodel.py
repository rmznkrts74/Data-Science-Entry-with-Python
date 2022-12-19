import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from modeladd import scaler

lastcallmodel=load_model("cycle.h5")
newCycle=[[1750,1751]]#yeni veriyle deneme
newCycle= scaler.transform(newCycle)
tryPredict=lastcallmodel.predict(newCycle)
print(tryPredict)
#[[953.7835]]
