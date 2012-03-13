from utils import PSet

config = PSet(
    ngraphs = 2,
    types = ["hist", "hist"], # hist or graph
    labels = ["SUSY", "QCD"],
    colors = ["r", "b"],
    markers = ["o", "s"],
    linestyles = ["-", "-"],
    datafile = "data.txt",
    name = "ecalIso",
    xlabel = "ECAL isolation (GeV)",
    ylabel = "fraction of events",
    xmin = 0.,
    xmax = 10.,
    ymin = 0.,
    ymax = 1.
)
