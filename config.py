from utils import PSet

ECAL_Isolation = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    datafile = "data/ecalIso.txt",
    name = "plots/ECAL_Isolation",
    xlabel = r"ECAL isolation (GeV)",
    ylabel = r"fraction of events",
    cutvalue = 4.2
)

HCAL_Isolation = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    datafile = "data/hcalIso.txt",
    name = "plots/HCAL_Isolation",
    xlabel = r"HCAL isolation (GeV)",
    ylabel = r"fraction of events",
    cutvalue = 2.2
)

Track_Isolation = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    datafile = "data/trackIso.txt",
    name = "plots/Track_Isolation",
    xlabel = r"Track isolation (GeV)",
    ylabel = r"fraction of events",
    cutvalue = 2.0
)

Hadronic_Over_EM = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    datafile = "data/hadronicOverEm.txt",
    name = "plots/Hadronic_Over_EM",
    xlabel = r"H/E",
    ylabel = r"fraction of events",
    cutvalue = 0.05
)

SigmaIetaIeta_EB = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    datafile = "data/sigmaIetaIeta_EB.txt",
    name = "plots/SigmaIetaIeta_EB",
    xlabel = r"Shower Shape",
    ylabel = r"fraction of events",
    cutvalue = 0.012
)

SigmaIetaIeta_EE = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    datafile = "data/sigmaIetaIeta_EE.txt",
    name = "plots/SigmaIetaIeta_EE",
    xlabel = r"Shower Shape",
    ylabel = r"fraction of events",
    cutvalue = 0.03
)
