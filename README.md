# OD_work
My own work files for the OD simulation development of Chroma (https://github.com/nEXO-collaboration/chroma-simulation) during summer 2021.

## General Files
#### LittleFunction.py / .ipynb
Contains a variety of functions I've used in different other files:
- renameSTLs(): Renames geometry STL files in a particular way
- ListForYaml(): Prints out wavelenght dependant values for the Yaml file in nice format for given wavelength bounds.
- getCherenkovWavelengthSample(): A working version of the CherenkovSimple() photon generator in Chroma
- ReadMuonsFromCSV(): a working version of Liam's code that is now in Chroma's Utilities.py, to read in the muon data

#### Plotting.ipynb
Development of the code that is now included in Chroma at Analysis/PlotPhotonPaths.py. This produces a 3D graph of all the photon paths, using the photonPath.txt file output that Chroma will produced if set to: `PropagationMode: Step`. **PlotPhotonPaths.py** is the py version of this that was then put into Chroma.

#### SimTiming.ipynb
Used to calculate average run times looking at photons/second processed.

#### compareH5.ipynb
Quick check to see if the seed used for all the random choses in our simulation changes, so that two runs with the same muons give the same averages but the exact photons produced are different.

#### hfiles_PMTs.ipynb
Uses the h5 output files from Chroma. Used to look at the timing of the photons as we will need this for muon tagging, as well as exploring the PMT channel data that is saved.

#### hfiles_photons.ipynb
Also uses the h5 output files, used for the development of many of the OD functions in Analysis/ODInput.py. Looking at the resulting wavelength distributions, over all light maps of hits as well as initial and final position 3D plots.

#### yamlFileWrite.ipynb
Playing around with writing to h5 files.

## Optics

#### OpticsGraphs.ipynb
Used to compare and collect the different wavelength dependant optical values to use in Yaml/OD/OpticalProperties_ODFull.yaml. Also print the chosen values into a format that can by pasted into the yaml file. Contains:
- Water: Absorption, scattering, Refractive Index
- Borosilicate (Pyrex glass) and Bialkali: " "

Along with using the data files saved below, in the code are also values:
- H2O data from nEXO-offline, https://github.com/nEXO-collaboration/nexo-offline/blob/6807b2f844f6f34215f4b9764626e35140838bfd/Simulation/DetSim/nEXOSim/src/nEXOMaterials.cc#L1101
- Some constants from scipy.constants, https://docs.scipy.org/doc/scipy/reference/constants.html
- Borosilicate (Pyrex) optical properties, according to DB XML files from Daya Bay DDDB/materials/pyrex.xml
- Bialkali optical properties for PMT photocathode, from Daya Bay collaboration sims use in nEXO-offline https://github.com/nEXO-collaboration/nexo-offline/blob/6807b2f844f6f34215f4b9764626e35140838bfd/Simulation/DetSim/nEXOSim/src/nEXOMaterials.cc#L1065

#### OpticsData/
Contains most of the optical data used from various sources. Overview of the optics data collection and the plan for each part of the OD geometry materials for chroma [here](./Optics/OpticsData/Materials%20and%20Optics.xlsx).

Fewell_AO348325_Data_File_1.csv - M.P. Fewell and A. von Trojan,"Absorption of light by water in the region of high transparency: recommended values for photon-transport calculation", Applied Optics, vol 58 (2019) pp. https://doi.org/10.1364/AO.58.002408

Huibers1997_Table1.csv - Paul D. T. Huibers, "Models for the wavelength dependence of the index of refraction of water," Appl. Opt. 36, 3785-3787 (1997)
https://www.osapublishing.org/ao/abstract.cfm?URI=ao-36-16-3785

SoudWaterProp.csv - Data just taken from points off of Soud's slides, https://nexowiki.llnl.gov/images/4/4c/NEXOCollaborationMeeting-ODSimulations2020.pdf slide 13

TransmittanceDAYA_BAY.csv - From Hamamatsu, contacted directly, spoke to Ardavan Ghassemi

scattering.csv -  Twardowski, M. S., et al. “Optical Backscattering Properties of the ‘Clearest’ Natural Waters.” Biogeosciences, vol. 4, no. 6, Nov. 2007, pp. 1041–58. bg.copernicus.org, https://doi.org/10.5194/bg-4-1041-2007. Table 2

## CherenkovGen
#### CherenkovLight.ipynb
Work done to take Soud's code (https://github.com/soudk/phys512/blob/master/project_cherenkov/NumbaCherenkov.ipynb) to develop the code to go in to Chroma to generate Cherenkov light from a muon.   
**CherenkovSource.py** was used to format some of this code into a format to actually be copied into Chroma
 
#### CherenkovTheory.ipynb
Details on the Cherenkov light wavelengths; number of photons; and looking at the PMT's QE to look at what range of wavelengths we need to simulate.

#### MuonResults.ipynb
Plots generated muons' entry and exit positions of the water tank. Also explored muon energy and speed.

## 
### Paths/
Contains text file output of the step by step output of each photon for small runs done early in the summer.

### h5_files/
Resulting .h5 files from OD Chroma runs during various stages of the development. 
