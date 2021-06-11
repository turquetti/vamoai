import statistics
import matplotlib.pyplot as plt

conjunto_1 = [1,2,3,4,5,6,7,8,9,10]
conjunto_2 = [11,12,13,14,15,16,17,18,19,20]

med_conjunto_1 = statistics.mean(conjunto_1)
med_conjunto_2 = statistics.mean(conjunto_2)

plt.scatter(conjunto_1, conjunto_2)
plt.show()

