import matplotlib.pyplot as plt
import prettyplotlib as ppl
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111)
np.random.seed(123)
data1 = np.random.normal(loc=1, size=(6,6), scale=0.2)
data2 = np.random.normal(size=(6,6), scale=0.2)
ppl.beeswarm([data1, data2], \
             colors=[ppl.colors.set1[1], ppl.colors.set1[2]], \
             xticklabels=["data1", "data2"])
ax.set_ylabel("Mean")
fig.savefig("plot.png")