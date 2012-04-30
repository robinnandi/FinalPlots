print "And we're off ..."
# Import stuff
import numpy as np
import matplotlib.pyplot as plt
import math
from config import SB_Bkgd_Est_4 as config
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
yerrors = [ [] for i in range(config.ngraphs) ] 

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
        print i
        yvalues[i].append(float(vec[2*i+1]))
        yerrors[i].append(float(vec[2*i+2]))
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
plt.subplot(211)
print "Plotting graphs ..."
for i in range(config.ngraphs):
    print xvalues
    print yvalues[i]
    if config.types[i] == "hist":
        plt.hist(xvalues, bins=bins, range=None, normed=False, weights=yvalues[i], color=config.colors[i], histtype="step", label=config.labels[i])
        plt.errorbar(xvalues, yvalues[i], yerr=yerrors[i], color=config.colors[i], marker=config.markers[i], linestyle="", label="")
    else:
        #plt.plot(xvalues, yvalues[i], color=config.colors[i], marker=config.markers[i], linestyle=config.linestyles[i], label=config.labels[i])
        plt.errorbar(xvalues, yvalues[i], yerr=yerrors[i], color=config.colors[i], marker=config.markers[i], linestyle=config.linestyles[i], label=config.labels[i])
    "Plotted graph "+str(i+1)+"."
ax = plt.gca()
print ax.get_ylim()
ymin = ax.get_ylim()[0]
ymax = ax.get_ylim()[1]

# Put in xlabel and ylabel
#plt.xlabel(config.xlabel)
plt.ylabel(config.ylabel)
plt.axis([xmin, xmax, ymin, ymax])
print "Set graph labels."

# Make legend
plt.legend()
plt.text(170, 0.3*ymax, config.note)
print "Done legend."

# Ratio plot
plt.subplot(212)
diff = np.zeros(nbins)
err = np.zeros(nbins)
for i in range(nbins):
    if yvalues[0][i] > 0:
        diff[i] = 100*(yvalues[1][i] - yvalues[0][i])/yvalues[0][i] 
        err[i] = 100*math.sqrt(yerrors[0][i]**2 + yvalues[0][i])/yvalues[0][i]
        #err[i] = 100*math.sqrt(yerrors[0][i]**2+yerrors[1][i]**2)/yvalues[0][i]
sum = 0
chi2 = 0
n = 0
for i in range(nbins):
    if err[i] > 0:
        n = n + 1/err[i]**2
        sum = sum + diff[i]/err[i]**2
        chi2 = chi2 + (diff[i]/err[i])**2
mean = sum/n
chi2ndof = chi2/nbins
error = 1/math.sqrt(n)
chi2 = 1.79
plt.errorbar(xvalues, diff, yerr=err, color="k", marker="o", linestyle="")
plt.plot([xmin, xmax], [mean, mean], color="k")
text = "\\begin{eqnarray}&&a = %.1f\pm%.1f\%s\\\\&&\chi^{2}/ndof = %.1f\\end{eqnarray}" % (mean, error, "%", chi2ndof)
print text
plt.text(60, 40, text)
plt.xlabel(config.xlabel)
plt.ylabel(r"difference (\%)")
plt.axis([xmin, xmax, -100, 100])

# Write to files
print "Saving files ..."
plt.savefig(config.name+".pdf")
print "Done. Exiting."
