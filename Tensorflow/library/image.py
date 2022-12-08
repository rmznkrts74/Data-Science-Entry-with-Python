import matplotlib.pyplot as plt
import numpy as np

listOfSalary=np.random.normal(4000,500,1000)##ilk maaş ikinci standart sapma,3 kişi sayısı
print(np.mean(listOfSalary))
plt.hist(listOfSalary,50)
plt.show()