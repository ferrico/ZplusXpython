import os
from ROOT import TFile
from helpers.analyzeZX import analyzeZX
from constants.analysis_params import (
#    LUMI_INT_2018_UL, LUMI_INT_2022preEE, LUMI_INT_2022postEE, n_sumgenweights_dataset_dct_jake, LUMI_INT_2023preBPix, LUMI_INT_2023postBPix
    n_sumgenweights_dataset_dct_jake, LUMI_INT_2018_UL, LUMI_INT_20220, LUMI_INT_20225, LUMI_INT_20230, LUMI_INT_20235
    )
#from sidequests.data.filepaths import (
#    mc_2017_UL_ZZ, mc_2017_UL_WZ,
#    data_2017_UL
#    )

# outdir_rootfile = "/blue/avery/rosedj1/ZplusXpython/data/20211017_new2018data"
outdir_rootfile = "/eos/user/y/yujil/HZZRun3Share/ZXCR/Data2022preEE/"
outdir_rootfile = "/eos/user/y/yujil/HZZRun3Share/ZXCR/Data2022postEE/"
outdir_rootfile = "./MinorOne/"
outdir_rootfile = "./Muon_MVAsip8_20230/"
suffix = "test_NEW"  # Underscore gets auto prefixed.
overwrite = 1
n_evts_to_process = -1

#lumi = LUMI_INT_2018_UL
#lumi = LUMI_INT_20220
#lumi = LUMI_INT_20225
lumi = LUMI_INT_20230
#lumi = LUMI_INT_20235

filename_dct = {
    #--- Nickname : filepath ---#

    ######## 2022preEE
#    "Data" : "/eos/user/y/yujil/HZZRun3Share/ZXCR/Data2022CD_noDuplicates.root",
#    "WZ" :  "/eos/user/y/yujil/HZZRun3Share/ZXCR/WZto3LNu_TuneCP5_13p6TeV_powheg",
    ######## 2022preEE


    ######## 2022postEE
#    "Data" : "/eos/user/y/yujil/HZZRun3Share/ZXCREFG/Data2022EFG_noDuplicates.root",
#    "WZ" :  "/eos/user/y/yujil/HZZRun3Share/ZXCREFG/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8.root"
    ######## 2022postEE

    ####### MinorOne
#    "WZ" : "/eos/user/f/ferrico/Muon_MVAsip8/20230/WZTo3LNu_M125_20230_skimmed.root",
    "Data" : "/eos/user/f/ferrico/Muon_MVAsip8/20230/Data_SingleMuonEgamma_20230_noDuplicates.root"
#    "Data"  :   "/eos/user/f/ferrico/MuonStudies_Run3/2023/Muon_ptCut/20230/Data_SingleMuonEgamma_20230_noDuplicates.root"
#    "Data" : "/eos/user/f/ferrico/MinorOne/Data_SingleMuonEgamma_minorOne_noDuplicates_2018.root",
    ####### MinorOne
    
    ####### TRUE MVA
#    "WZ" : "/eos/user/f/ferrico/Muon_MVA_TRUE/WZTo3LNu_MinorOne_MVA.root",
#    "Data" : "/eos/user/f/ferrico/MuonSttudies_2018/Muon_MVA_TRUE/Data_SingleMuonEgamma_minorOne_MVA_noDuplicates_2018.root", 
    ####### TRUE MVA

    # "DY50" : "/cmsuf/data/store/user/t2/users/rosedj1/HiggsMassMeasurement/Samples/skim2L/MC/fullstats/ZL_ZLL_CR/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_2018.root",  # n_evts_tot = 2,647,699
    # ### "WZ"   : "/cmsuf/data/store/user/t2/users/rosedj1/HiggsMassMeasurement/Samples/skim2L/MC/fullstats/ZL_ZLL_CR/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_realistic_v15-v1_2018.root",  # n_evts_tot = 819,364
    # "WZ-ext1-v2" : "/cmsuf/data/store/user/t2/users/rosedj1/HiggsMassMeasurement/Samples/skim2L/MC/fullstats/ZL_ZLL_CR/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_realistic_v15_ext1-v2_2018.root",
    # ### "WZ_vukasin"   : "/blue/avery/rosedj1/ZplusXpython/data/vukasin/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIIAutumn18MiniAOD-102X_2018_filter2l_new_ZX.root",
    # "ZZ"   : "/cmsuf/data/store/user/t2/users/rosedj1/HiggsMassMeasurement/Samples/skim2L/MC/fullstats/ZL_ZLL_CR/ZZTo4L_TuneCP5_13TeV_powheg_pythia8_2018.root",  # n_evts_tot = 7,287,720
}

kinem_ls = [
    "mass4l", 
    #"mass4lREFIT", "mass4lREFIT_vtx_BS",
    # "mass4lErr", "mass4lErrREFIT", "mass4lErrREFIT_vtx_BS",
    # "met", "D_bkg_kin", "D_bkg_kin_vtx_BS"
    ]

print("First stage of processing (FR computation and CR histogram creation) has been initiated.\n")

print("!!! USING WRONG LUMI_INT !!!")

for name, filepath in filename_dct.items():
    inFile = TFile.Open(filepath, "READ")
    try:
        tree = inFile.Get("Ana/passedEvents") # for MINIAOD
        tree = inFile.Get("Events") # for NANOAOD
        n_evts = tree.GetEntries()
        h_num_eventi = inFile.Get("sumWeights");
        n_dataset_tot = h_num_eventi.Integral();
        print("n_dataset_tot = " + str(n_dataset_tot))
    except (AttributeError, ReferenceError):
        # Probably the wrong path to TTree.
        tree = inFile.Get("passedEvents") #for MINIAOD
        n_evts = tree.GetEntries() 
    print(
        f"File: {filepath} has been opened.\n"
        f"-- Nickname: {name}\n"
        f"-- Found {n_evts} events."
        )
    if "Data" not in name:
        print(
            f"-- MC file has sumGenWeights="
            f"{n_sumgenweights_dataset_dct_jake[name]}."
            )
    analyzeZX(tree=tree, Nickname=name, outfile_dir=outdir_rootfile, suffix=suffix,
               overwrite=overwrite, lumi=lumi, kinem_ls=kinem_ls,
               n_evts_to_process=n_evts_to_process)
    inFile.Close()
