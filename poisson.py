import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.random.poisson(11.9, 10000)
plt.hist(x,100)
plt.savefig("poisson.pdf")
