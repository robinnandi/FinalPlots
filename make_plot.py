# Import stuff
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
from config import Jet_Pt_Resolution as config

# Create the figure
fig = plt.figure()

# Open the file containing the data
f = open(config.datafile, "r")

# Declare xvalues and yvalues to be filled
xvalues = []
yvalues = [ [] for i in range(config.ngraphs) ] 
yerrors = [ [] for i in range(config.ngraphs) ] 

# Read data from the file first element is x value bin centre the others are
# various different graphs.
for line in f:
    line = line.rstrip("\n")
    print line
    vec = line.split(", ")
    xvalues.append(float(vec[0]))
    for i in range(config.ngraphs):
        yvalues[i].append(float(vec[2*i+1]))
        yerrors[i].append(float(vec[2*i+2]))

# Define the binning
nbins = len(xvalues)
binwidth = round(xvalues[1] - xvalues[0], 5)
xmin = round(xvalues[0]-binwidth/2, 5)
xmax = round(xmin + binwidth*nbins, 5)
bins = np.arange(xmin, xmax+binwidth, binwidth)

try:
    if config.adjustmargins == True:
        axes = plt.Axes(fig, [.1,.15,.8,.75])
        fig.add_axes(axes)
except:
    print "Default margins used."

# Plot the graphs
for i in range(config.ngraphs):
    if config.types[i] == "hist":
        plt.hist(xvalues, bins=bins, range=None, normed=False, weights=yvalues[i], histtype=config.histtypes[i], color=config.colors[i], label=config.labels[i])
        plt.errorbar(xvalues, yvalues[i], yerr=yerrors[i], color=config.colors[i], marker=config.markers[i], linestyle="", label="")
    elif config.types[i] == "plot":
        #plt.plot(xvalues, yvalues[i], color=config.colors[i], marker=config.markers[i], linestyle=config.linestyles[i], label=config.labels[i])
        plt.errorbar(xvalues, yvalues[i], yerr=yerrors[i], color=config.colors[i], marker=config.markers[i], linestyle=config.linestyles[i], label=config.labels[i])
    else:
        print "Graph type not recognised."

# Axes
ax = plt.gca()
print ax.get_ylim()
try:
    xmin = config.xmin
    xmax = config.xmax
except:
    print "Default x-axis range used."
ymin = ax.get_ylim()[0]
ymax = ax.get_ylim()[1]
try:
    if config.xlog == True:
        ax.set_xscale("log")
        ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
    if config.ylog == True:
        ax.set_yscale("log")
        ax.yaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
except:
    print "Linear scale used by default."

# Plot a vertical line representing the cut value
try:
    plt.plot([config.cutvalue, config.cutvalue], [ymin, ymax], "k-", label="cut value")
except:
    print "Cut value not specified."

# Fill error band
try:
    if config.fill == True:
        ax.fill_between(xvalues, yvalues[0], yvalues[2], facecolor="y")
        plt.errorbar([config.point[0]], [config.point[1]], xerr=[config.err], color="k", marker="o")
except:
    print "Not filled."

# Put in xlabel and ylabel
plt.xlabel(config.xlabel)
plt.ylabel(config.ylabel)
plt.axis([xmin, xmax, ymin, ymax])

# Make legend
plt.legend()

# Write to files
plt.savefig(config.name+".pdf")
