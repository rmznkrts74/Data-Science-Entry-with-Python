import numpy as np
import pandas as pd
##Series
my_dict={
    "Dark":50,
    "white":30,
    "grey":20
}
x=pd.Series(my_dict)#sözlüğü excel cıktısı gibi gösterir
#print(x)
myList=[50,40,30]
my_name=["Dark","Dark2","Dark3"]
y=pd.Series(myList,my_name)
#or
y=pd.Series(data=myList,index=my_name)
#print(y)
numpyDizisi=np.array(myList)
print(numpyDizisi)
x=pd.Series(numpyDizisi)
print(x)