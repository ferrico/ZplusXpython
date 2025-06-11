#include <iostream>
#include <set>
#include <TString.h>
#include <TFile.h>
#include <TTree.h>

void remove_duplicates_Filippo() {
    // path / name of root file
    TString prefix = "/eos/user/f/ferrico/Muon_MVAsip8/20230/Data1_Run2023C_v4";
	///eos/user/f/ferrico/Muon_MVA/Data_SingleMuonEgamma_minorOne_MVA";
    TString filename = prefix+".root";
    TString pathToTree = "Ana/passedEvents";

    std::cout<<filename<<std::endl;

    TFile *oldfile = new TFile(filename);
    TTree *oldtree = (TTree*)oldfile->Get("Events"); // NANOAOD
    TH1F* ha = new TH1F("sumWeights","sumWeights",1,-0.5,0.5);
    Long64_t nentries = oldtree->GetEntries();
    std::cout<<nentries<<" total entries."<<std::endl;
//    ULong64_t Run, LumiSect;
    UInt_t Run, LumiSect; // NANOAOD
    ULong64_t Event;
    bool passedZ4lSelection;
//    oldtree->SetBranchAddress("Run",&Run);
//    oldtree->SetBranchAddress("LumiSect",&LumiSect);
//    oldtree->SetBranchAddress("Event",&Event);
    oldtree->SetBranchAddress("run",&Run); // NANOAOD
    oldtree->SetBranchAddress("luminosityBlock",&LumiSect);
    oldtree->SetBranchAddress("event",&Event);
    //Create a new file + a clone of old tree in new file

    TFile *newfile = new TFile(
            prefix+"_noDuplicates.root"
            ,"recreate");
    TTree *newtree = oldtree->CloneTree(0);

    std::set<TString> runlumieventSet;
    int nremoved = 0;
    for (Long64_t i=0;i<nentries; i++) {
        if (i%2500000==0) std::cout<<i<<"/"<<nentries<<std::endl;
        oldtree->GetEntry(i);
//if(Run==305821 && Event==455992205 && LumiSect==282)
//	std::cout<<"trovato l'event"<<std::endl;
        TString s_Run  = std::to_string(Run);
        TString s_Lumi = std::to_string(LumiSect);
        TString s_Event = std::to_string(Event);
        TString runlumievent = s_Run+":"+s_Lumi+":"+s_Event;
        
        if (runlumieventSet.find(runlumievent)==runlumieventSet.end()) {
            runlumieventSet.insert(runlumievent);
            newtree->Fill();

//for(auto it = runlumieventSet.begin(); it != runlumieventSet.end(); it++)
//    {
//        cout << *it << endl;
//    }
//std::cout<<"-----"<<std::endl;
			    if(Run==362728 && Event==53398870 && LumiSect==27)
				std::cout<<"\t\t - lo sto prendendo"<<std::endl;
        } else {
            nremoved++;
			    if(Run==362728 && Event==53398870 && LumiSect==27)
			        std::cout<<"\t\t - lo sto scartando"<<std::endl;
        }
        //if (passedZ4lSelection) newtree->Fill();


//	if(i > 100)
//			return;
    }

    std::cout<<nremoved<<" duplicates."<<std::endl;
    newtree->Print();
    newtree->AutoSave();
    ha->Write();
    //delete oldfile;
    delete newfile;
}
