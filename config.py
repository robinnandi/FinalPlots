from utils import PSet

ECAL_Isolation = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    types = ["hist", "hist"],
    histtypes = ["step", "step"],
    colors = ["b", "g"],
    linestyles = ["-", "-"],
    markers = ["", ""],
    xlog = False,
    ylog = False,
    datafile = "data/ecalIso.txt",
    name = "plots/ECAL_Isolation",
    xlabel = r"ECAL isolation (GeV)",
    ylabel = r"fraction of events",
    cutvalue = 4.2
)

HCAL_Isolation = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    types = ["hist", "hist"],
    histtypes = ["step", "step"],
    colors = ["b", "g"],
    linestyles = ["-", "-"],
    markers = ["", ""],
    datafile = "data/hcalIso.txt",
    name = "plots/HCAL_Isolation",
    xlabel = r"HCAL isolation (GeV)",
    ylabel = r"fraction of events",
    cutvalue = 2.2
)

Track_Isolation = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    types = ["hist", "hist"],
    histtypes = ["step", "step"],
    colors = ["b", "g"],
    linestyles = ["-", "-"],
    markers = ["", ""],
    datafile = "data/trackIso.txt",
    name = "plots/Track_Isolation",
    xlabel = r"Track isolation (GeV)",
    ylabel = r"fraction of events",
    cutvalue = 2.0
)

Hadronic_Over_EM = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    types = ["hist", "hist"],
    histtypes = ["step", "step"],
    colors = ["b", "g"],
    linestyles = ["-", "-"],
    markers = ["", ""],
    datafile = "data/hadronicOverEm.txt",
    name = "plots/Hadronic_Over_EM",
    xlabel = r"H/E",
    ylabel = r"fraction of events",
    cutvalue = 0.05
)

SigmaIetaIeta_EB = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    types = ["hist", "hist"],
    histtypes = ["step", "step"],
    colors = ["b", "g"],
    linestyles = ["-", "-"],
    markers = ["", ""],
    datafile = "data/sigmaIetaIeta_EB.txt",
    name = "plots/SigmaIetaIeta_EB",
    xlabel = r"Shower Shape",
    ylabel = r"fraction of events",
    cutvalue = 0.012
)

SigmaIetaIeta_EE = PSet(
    ngraphs = 2,
    labels = ["SUSY", "QCD"],
    types = ["hist", "hist"],
    histtypes = ["step", "step"],
    colors = ["b", "g"],
    linestyles = ["-", "-"],
    markers = ["", ""],
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

Trigger_Efficiency_HT = PSet(
    ngraphs = 1,
    labels = [""],
    types = ["plot"],
    colors = ["k"],
    linestyles = [""],
    markers = ["."],
    datafile = "data/Trigger_Efficiency_HT.txt",
    name = "plots/Trigger_Efficiency_HT",
    xlabel = r"$H_{T}~(GeV)$",
    ylabel = r"Efficiency"
)

Trigger_Efficiency_PhotonPt = PSet(
    ngraphs = 1,
    labels = [""],
    types = ["plot"],
    colors = ["k"],
    linestyles = [""],
    markers = ["."],
    datafile = "data/Trigger_Efficiency_PhotonPt.txt",
    name = "plots/Trigger_Efficiency_PhotonPt",
    xlabel = r"Photon $p_{T}~(GeV)$",
    ylabel = r"Efficiency"
)

Jet_Pt_Threshold = PSet(
    ngraphs = 2,
    labels = ["Signal", "Background"],
    types = ["plot", "plot"],
    colors = ["k", "b"],
    linestyles = ["-", "-"],
    markers = ["", ""],
    datafile = "data/Jet_Pt_Threshold.txt",
    name = "plots/Jet_Pt_Threshold",
    xlabel = r"Jet $p_{T}$ threshold (GeV)",
    ylabel = r"Efficiency"
)

nVertices_Data = PSet(
    ngraphs = 1,
    labels = ["Data"],
    types = ["hist"],
    histtypes = ["stepfilled"],
    colors = ["b"],
    linestyles = [""],
    markers = [""],
    datafile = "data/nVertices_Data.txt",
    name = "plots/nVertices_Data",
    xlabel = r"Number of Vertices",
    ylabel = r"fraction of events"
)

nVertices_MC = PSet(
    ngraphs = 1,
    labels = ["MC"],
    types = ["hist"],
    histtypes = ["stepfilled"],
    colors = ["b"],
    linestyles = [""],
    markers = [""],
    datafile = "data/nVertices_MC.txt",
    name = "plots/nVertices_MC",
    xlabel = r"Number of Vertices",
    ylabel = r"fraction of events"
)

JES_Unc_pT = PSet(
    ngraphs = 1,
    labels = ["$|\eta| < 0.3$"],
    types = ["plot"],
    colors = ["b"],
    linestyles = ["-"],
    markers = ["."],
    xmin = 10,
    xmax = 500,
    xlog = True,
    ylog = False,
    datafile = "data/JES_Unc_pT.txt",
    name = "plots/JES_Unc_pT",
    xlabel = r"Jet $p_{T}$ (GeV)",
    ylabel = r"Jet Energy Scale Uncertainty (\%)"
)

JES_Unc_Eta = PSet(
    ngraphs = 1,
    labels = ["$p_{T} = 100~GeV$"],
    types = ["plot"],
    colors = ["b"],
    linestyles = ["-"],
    markers = ["."],
    xmin = -5,
    xmax = 5,
    xlog = False,
    ylog = False,
    datafile = "data/JES_Unc_Eta.txt",
    name = "plots/JES_Unc_Eta",
    xlabel = r"Jet $\eta$",
    ylabel = r"Jet Energy Scale Uncertainty (\%)"
)
