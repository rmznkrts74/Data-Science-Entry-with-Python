import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
ageList=[10,20,30,30,50,40,50,60,70,75]
weightList=[30,40,55,75,86,92,61,89,90,75]
numpyAgeList=np.array(ageList)
numpyWeightList=np.array(weightList)

plt.plot(numpyAgeList,numpyWeightList,"r")#r redi temsil ediyor ilk yazılan X ikinci Y
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age-Weight")
plt.show()
