print "And we're off ..."
# Import stuff
import numpy as np
import matplotlib.pyplot as plt
from config import SigmaIetaIeta_EB as config
print "Imported files."

# Create the figure
fig = plt.figure()
print "Made figure."

# Open the file containing the data
f = open(config.datafile, "r")
print "Opened file."

# Declare xvalues and yvalues to be filled
xvalues = []
yvalues = [ [] for i in range(config.ngraphs) ] 

# Read data from the file first element is x value bin centre the others are
# various different graphs.
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

# Define the binning
nbins = len(xvalues)
binwidth = round(xvalues[1] - xvalues[0], 5)
xmin = round(xvalues[0]-binwidth/2, 5)
xmax = round(xmin + binwidth*nbins, 5)
print xmax
bins = np.arange(xmin, xmax+binwidth, binwidth)
print bins

# Plot the graphs
print "Plotting graphs ..."
for i in range(config.ngraphs):
    print xvalues
    print yvalues[i]
    plt.hist(xvalues, bins=bins, range=None, normed=False, weights=yvalues[i], histtype="step", label=config.labels[i])
    "Plotted graph "+str(i+1)+"."
ax = plt.gca()
print ax.get_ylim()
ymin = ax.get_ylim()[0]
ymax = ax.get_ylim()[1]

# Plot a vertical line representing the cut value
plt.plot([config.cutvalue, config.cutvalue], [ymin, ymax], "k-", label="cut value")
print "Finished plotting graphs."

# Put in xlabel and ylabel
plt.xlabel(config.xlabel)
plt.ylabel(config.ylabel)
plt.axis([xmin, xmax, ymin, ymax])
print "Set graph labels."

# Make legend
plt.legend()
print "Done legend."

# Write to files
print "Saving files ..."
plt.savefig(config.name+".png")
plt.savefig(config.name+".eps")
plt.savefig(config.name+".pdf")
print "Done. Exiting."
