from utils import PSet

ECAL_Isolation = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    datafile = "data/ECAL_Isolation.txt",
    name = "plots/ECAL_Isolation",
    xlabel = r"\textbf{ECAL isolation (GeV)}",
    ylabel = r"\textbf{fraction of events}",
)
