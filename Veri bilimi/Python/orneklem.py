import numpy as np
populasyon = np.random.randint(0,80,10000)
"""#print(populasyon[0:10])
#orneklem cekimi
np.random.seed(115)"""
orneklem=np.random.choice(a=populasyon,size=100)
"""print(orneklem[0:10])
print(orneklem.mean())#ortalama
print(populasyon.mean())"""
#orneklem dagılımı
np.random.seed(10)
orneklem1=np.random.choice(a=populasyon,size=100)
orneklem2=np.random.choice(a=populasyon,size=100)
orneklem3=np.random.choice(a=populasyon,size=100)
orneklem4=np.random.choice(a=populasyon,size=100)
orneklem5=np.random.choice(a=populasyon,size=100)
orneklem6=np.random.choice(a=populasyon,size=100)
orneklem7=np.random.choice(a=populasyon,size=100)
orneklem8=np.random.choice(a=populasyon,size=100)
orneklem9=np.random.choice(a=populasyon,size=100)
orneklem10=np.random.choice(a=populasyon,size=100)
average=(orneklem10.mean()+orneklem9.mean()+orneklem8.mean()+orneklem7.mean()+orneklem6.mean()+orneklem5.mean()+orneklem4.mean()+orneklem3.mean()+orneklem2.mean()+orneklem1.mean())/10
print(average)
