source setup_lxplus.sh 
python3 scripts/main_FR_CR.py
vi constants/analysis_params.py 
python3 scripts/WZremoval_from_FR_comp.py

python3  scripts/plotters/plot_fakerate_hists.py -w /eos/user/y/yujil/HZZRun3Share/ZXCR/Data2022CD_noDuplicates/Hist_Data_test01_WZremoved.root -o ./test.pdf -d /eos/user/y/yujil/HZZRun3Share/ZXCR/Data2022CD_noDuplicates/Hist_Data_test01.root -y 2018
python3 scripts/main_estimateZX_ntuples.py
python3 scripts/estimate_final_numbers_macro.py
python3 scripts/plotting_macros.py


vi ./sidequests/funcs/evt_loops.py -----> NON HA DIPENDENZA DA LUMI 
vi ./skimmers/select_evts_OSmethod_multiquartetperevt.py ----> change filename here sidequests/data/filepaths.py
############# ---> MVA here
classes/mylepton.py
############# ---> MVA here
hadd -f ZX_2018_MinorOne.root test__2018_Data_2018.root test__2018_ZZ_2018.root
haddnano --> FOR NANOAOD


### for MVA:
vi ./scripts/helpers/analyzeZX.py
vi ./scripts/helpers/estimateZX.py ---> NON USATO
vi ./skimmers/skim_ZLL_addbranches.py
vi classes/mylepton.py 

### Removal
vi ./skimmers/remove_duplicates_Filippo.C  
