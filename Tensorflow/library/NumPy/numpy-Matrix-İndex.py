import numpy as np
##matrix
newList=[[10,20,30],[20,30,40],[40,50,60]]
newMatrixArray=np.array(newList)
print(newMatrixArray[2][1])#matrix[satır][kolon]
#newMatrixArray[2][1]=newMatrixArray[2,1]
#*********Slicing*************
print(newMatrixArray[1:,2])#1 den son satıra kadar 2 kolondaki elemanları getirir
print(newMatrixArray[1:,2:])
newList=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24]]
newMatrix=np.array(newList)
print(newMatrix[2])#2 indexli satırı verir
print(newMatrix[[0,2,4]])#her kolonda 0 2 4 indexli sayılar gelir
