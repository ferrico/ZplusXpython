import ROOT
from scripts.helpers.estimateZX import estimateZX
from constants.analysis_params import LUMI_INT_2022postEE,LUMI_INT_2018_UL
from sidequests.data.filepaths import fakerates_WZremoved

# outfile_dir = "/blue/avery/rosedj1/ZplusXpython/data/controlreg_OS/20210802"
outdir_rootfile = "/eos/user/y/yujil/HZZRun3Share/ZXCR/Data2022preEE/"
outdir_rootfile = "/eos/user/y/yujil/HZZRun3Share/ZXCR/Data2022postEE/"
outdir_rootfile = "./MinorOne/"
outfile_dir = "./MinorOne/"
suffix = ""
overwrite = 0

# file_WZremoved = "Hist_Data_ptl3_WZremoved.root"
file_fakerates_WZremoved = fakerates_WZremoved

filename_dct = {

    #### 2022preEE
    #"Data" : "/eos/user/y/yujil/HZZRun3Share/ZXCR/Data2022CD_noDuplicates.root",
    #"ZZ"   : "/eos/user/y/yujil/HZZRun3Share/ZXCR/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8.root",
    #"TT"   : "/eos/user/y/yujil/HZZRun3Share/ZXCR/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8.root",
    #"DY50"   : "/eos/user/y/yujil/HZZRun3Share/ZXCR/DYTo2L_MLL-50_TuneCP5_13p6TeV_pythia8.root",
    #### 2022preEE

    #### 2022postEE
#    "Data" : "/eos/user/y/yujil/HZZRun3Share/ZXCREFG/Data2022EFG_noDuplicates.root",
#    "ZZ" : "/eos/user/y/yujil/HZZRun3Share/ZXCREFG/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8.root",
#    "TT" : "/eos/user/y/yujil/HZZRun3Share/ZXCREFG/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8.root",
#    "DY50" : "/eos/user/y/yujil/HZZRun3Share/ZXCREFG/DYJetsToLL_M-50_TuneCP5_13p6TeV-madgraphMLM-pythia8.root",
    #### 2022postEE


    #### Run 2
    "Data" : "/eos/user/f/ferrico/MinorOne/Data_SingleMuonEgamma_minorOne_noDuplicates.root",
    "ZZ" : "/eos/user/f/ferrico/MinorOne/ZZTo4L_MinorOne.root",
    "TT" : "/eos/user/f/ferrico/MinorOne/TTTo2L2Nu_MinorOne.root",
    "DY50" : "/eos/user/f/ferrico/MinorOne/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX_minorOne.root",
    #### Run 2

    }

print("\nSecond stage of processing (Creation of ZX SR contributions for Data and ZZ.\n")

for name, filepath in filename_dct.items():
    inFile =  ROOT.TFile.Open(filepath, "READ")
    tree = inFile.Get("Events")
    tree = inFile.Get("passedEvents")
    n_evts = tree.GetEntries()
    print(
        f"Successfully opened file:\n"
        f"-- {filepath}\n"
        f"-- Nickname: {name}"
        f"-- Found {n_evts} events in TTree."
    )
    estimateZX(FakeRateFile=file_fakerates_WZremoved, tree=tree,
               Nickname=name, outfile_dir=outfile_dir, suffix=suffix,
               overwrite=overwrite, lumi=LUMI_INT_2018_UL)#LUMI_INT_2022postEE)
    inFile.Close()
