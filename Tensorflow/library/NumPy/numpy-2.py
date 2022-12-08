##numpy some methods
import  numpy as np
##arange***önemli
print(np.arange(0,10))#örnek liste olusturur
print(np.arange(0,10,2))
##zeros sıfır olusturuyor girilen sayı kadar
print(np.zeros((5,5)))#tek parametre olursa liste şeklinde iki olursa matriks şeklinde
##ones zeros gibi ama bu 1 yazdırıyor
##linspace****önemli
print(np.linspace(0,20,5))#sondaki sayı kaç sayıdan olusacagını beliritiyor.eşit aralıklara bölüyor
##eye birim matrix olusturuyor
print(np.eye(10))