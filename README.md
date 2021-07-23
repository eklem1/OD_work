# OD_work
My own work files for the OD simulation development of Chroma (https://github.com/nEXO-collaboration/chroma-simulation) during summer 2021.

## General Files
#### Plotting.ipynb
Development of the code that is now included in Chroma at Analysis/PlotPhotonPaths.py. This produces a 3D graph of all the photon paths, using the photonPath.txt file output that Chroma will produced if set to: `PropagationMode: Step`. **PlotPhotonPaths.py** is the py version of this that was then put into Chroma.

#### hfiles_PMTs.ipynb
Uses the h5 output files from Chroma. Used to look at the timing of the photons as we will need this for muon tagging, as well as exploring the PMT channel data that is saved.

#### hfiles_photons.ipynb
Also uses the h5 output files, used for the development of many of the OD functions in Analysis/ODInput.py. Looking at the resulting wavelength distributions, over all light maps of hits as well as initial and final position 3D plots.

#### LittleFunction.py / .ipynb
Contains a variety of functions I've used in different other files:
- renameSTLs(): Renames geometry STL files in a particular way
- ListForYaml(): Prints out wavelenght dependant values for the Yaml file in nice format for given wavelength bounds.
- getCherenkovWavelengthSample(): A working version of the CherenkovSimple() photon generator in Chroma
- ReadMuonsFromCSV(): a working version of Liam's code that is now in Chroma's Utilities.py, to read in the muon data

#### SimTiming.ipynb
Used to calculate average run times looking at photons/second processed.

#### yamlFileWrite.ipynb
Playing around with writing to h5 files.

## Optics

#### OpticsGraphs.ipynb
Used to compare and collect the different wavelength dependant optical values to use in Yaml/OD/OpticalProperties_ODFull.yaml. Also print the chosen values into a format that can by pasted into the yaml file. Contains:
- Water: Absorption, scattering, Refractive Index
- Borosilicate (Pyrex glass) and Bialkali: " "

#### OpticsData/
Contains most of the optical data used from various sources. ADD SOURCES


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
