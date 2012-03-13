import matplotlib.pyplot as plt
from config import config

fig = plt.figure()
f = open(config.datafile, "r")
xvalues = []
yvalues = [ [] for i in range(config.ngraphs) ] 
for line in f:
    line.rstrip("\n")
    vec = line.split(", ")
    xvalues.append(vec[0])
    for i in range(config.ngraphs):
        yvalues[i].append(vec[i+1])
nbins = len(xvalues)
for i in range(config.ngraphs):
    plt.plot(xvalues, yvalues[i], marker=config.markers[i], linestyle=config.linestyles[i], color=config.colors[i], label=config.labels[i])
plt.xlabel(config.xlabel)
plt.ylabel(config.ylabel)
plt.axis([config.xmin, config.xmax, config.ymin, config.ymax])
plt.legend()
plt.show()
plt.savefig(config.name+".png")
