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

SB_Bkgd_Est_1 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/SB_Bkgd_Est_1.txt",
    name = "plots/SB_Bkgd_Est_1",
    note = r"$400<H_{T}<500~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

SB_Bkgd_Est_2 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/SB_Bkgd_Est_2.txt",
    name = "plots/SB_Bkgd_Est_2",
    note = r"$500<H_{T}<600~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

SB_Bkgd_Est_3 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/SB_Bkgd_Est_3.txt",
    name = "plots/SB_Bkgd_Est_3",
    note = r"$600<H_{T}<700~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

SB_Bkgd_Est_4 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/SB_Bkgd_Est_4.txt",
    name = "plots/SB_Bkgd_Est_4",
    note = r"$H_{T}>700~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

MC_Bkgd_Est_1 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/MC_Bkgd_Est_1.txt",
    name = "plots/MC_Bkgd_Est_1",
    note = r"$400<H_{T}<500~GeV$",
    xlabel = r"$\slashed{E}_{T}$~(GeV)",
    ylabel = r"number of events"
)

MC_Bkgd_Est_2 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/MC_Bkgd_Est_2.txt",
    name = "plots/MC_Bkgd_Est_2",
    note = r"$500<H_{T}<600~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

MC_Bkgd_Est_3 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/MC_Bkgd_Est_3.txt",
    name = "plots/MC_Bkgd_Est_3",
    note = r"$600<H_{T}<700~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

MC_Bkgd_Est_4 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/MC_Bkgd_Est_4.txt",
    name = "plots/MC_Bkgd_Est_4",
    note = r"$H_{T}>700~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

Bkgd_Est_1 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/Bkgd_Est_1.txt",
    name = "plots/Bkgd_Est_1",
    note = r"$400<H_{T}<500~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

Bkgd_Est_2 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/Bkgd_Est_2.txt",
    name = "plots/Bkgd_Est_2",
    note = r"$500<H_{T}<600~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

Bkgd_Est_3 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/Bkgd_Est_3.txt",
    name = "plots/Bkgd_Est_3",
    note = r"$600<H_{T}<700~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)

Bkgd_Est_4 = PSet(
    ngraphs = 2,
    labels = ["Predicted", "Observed"],
    types = ["hist", "plot"],
    colors = ["b", "k"],
    linestyles = ["-", ""],
    markers = ["", "."],
    datafile = "data/Bkgd_Est_4.txt",
    name = "plots/Bkgd_Est_4",
    note = r"$H_{T}>700~GeV$",
    xlabel = r"$\slashed{E}_{T}~(GeV)$",
    ylabel = r"number of events"
)
