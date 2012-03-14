print "And we're off ..."
import numpy as np
import matplotlib.pyplot as plt
from config import ECAL_Isolation as config
print "Imported files."

fig = plt.figure()
print "Made figure."
f = open(config.datafile, "r")
print "Opened file."
xvalues = []
yvalues = [ [] for i in range(config.ngraphs) ] 
print "Loop through lines in file ..."
j = 1
for line in f:
    print "At line "+str(j)+"."
    line = line.rstrip("\n")
    print line
    vec = line.split(", ")
    xvalues.append(float(vec[0]))
    for i in range(config.ngraphs):
        yvalues[i].append(float(vec[i+1]))
    j = j + 1
nbins = len(xvalues)
binwidth = xvalues[1] - xvalues[0]
xmin = xvalues[0]-binwidth/2
xmax = xmin + binwidth*nbins
bins = np.arange(xmin, xmax+binwidth, binwidth)
print bins
print "Plotting graphs ..."
for i in range(config.ngraphs):
    print xvalues
    print yvalues[i]
    plt.hist(xvalues, bins=bins, range=None, normed=False, weights=yvalues[i], histtype="step", label=config.labels[i])
    "Plotted graph "+str(i+1)+"."
print "Finished plotting graphs."
plt.xlabel(config.xlabel)
plt.ylabel(config.ylabel)
print "Set graph labels."
plt.legend()
print "Done legend."
plt.savefig(config.name+".png")
