import statistics
import matplotlib.pyplot as plt
import numpy as np

func1 = [10,34,35,36,11,2,67,32,12]
func2 = [3,44,72,12,65,78,34,67,54]

mean_func1 = statistics.mean(func1)
mean_func2 = statistics.mean(func2)

#média
print(f"Média da pessoa funcionária 1: {mean_func1}")
print(f"Média da pessoa funcionária 2: {mean_func2}")

#plot
# n = 9
# x = np.random.rand(n)

plt.scatter(func1, func2)
plt.show()
