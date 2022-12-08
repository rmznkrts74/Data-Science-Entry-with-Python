import pandas as pd
import numpy as np
firstindex=["Simpson","Simpson","Simpson","South Park","South Park","South Park",]
innerIndex=["Homer","Bart","Marge","Cartman","Kenny","Kyle"]
compactIndex=list(zip(firstindex,innerIndex))
compactIndex=pd.MultiIndex.from_tuples(compactIndex)
print(compactIndex)
mycartoonList=[[40,"A"],[10,"B"],[30,"C"],[9,"D"],[10,"E"],[11,"F"]]
cartoonNumpy=np.array(mycartoonList)
cartoonDataFrame=pd.DataFrame(cartoonNumpy,index=compactIndex,columns=["Age","Job"])
print(cartoonDataFrame)
print(cartoonDataFrame.loc["Simpson"])#simpson bölümü gelir
print(cartoonDataFrame.loc["Simpson"]["Age"])#simpsondaki agei getirir
cartoonDataFrame.index.names=["Names Of Cartoon","Name"]#iki sutuna isim ekledik
print(cartoonDataFrame)
