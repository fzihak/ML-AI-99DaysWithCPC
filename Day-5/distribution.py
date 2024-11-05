import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(data, bins=30, density=True)
plt.title("Normal Distribution")
plt.show()
