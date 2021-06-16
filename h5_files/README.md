# OD - nEXO's Outer Detector 

These files are all for running simulations of the photons produced by muons passing through nEXO's water tank, or outer detector. All relevant geometry files can be found in  [~/Geometry/OD/](https://github.com/nEXO-collaboration/chroma-simulation/tree/eklem1/issue_6/Geometry/OD) and it's subfolders.

### Detector files
These files set up the geometry, its positioning and set what material each part is made of. They set the required locations for the imported stl files; the optical property files; where the data should be saved to and any other data files needed. They also specify what generator is used to create photons. 

The CherenkovSimple Generator should be used to generate photons from a single muon's path.
```
Simulation:                      
  Generator: CherenkovSimple; [0,-1,-1]; 200  #type of Generator; 'muon' momentum; length of muon track in mm
  NumberOfPhotons: 200                        # number of photons per event - really you should set it to 10*(length of muon track) as Cherenkov light should generate ~10 photons/mm in water
  NumberOfSources: 1                          # number of events 
  NumberOfRuns: 1                             # number of runs define how often NumberOfPhotons x NumberOfSources will be simulated
  PhotonLocation:  Point=0,0,-3400            #Define start position of muon track
```
This is currently being developed to take in a list of muons paths that are simulated seperately and then generate the Cherenkov photons.

#### OD.yaml
This file should run the most updated version of the full OD simulation.

#### OD_Rem.yaml
This file sets up to run a simulation with a simplified geometry to replicate Remington's work ([found here](https://nexowiki.llnl.gov/images/5/53/NEXO_OD_Muon_Veto_Efficiency_v1.0.pdf)). The PMTs here are simple half hemispheres and it uses the simplified optical properties found in OpticalProperties_OD_Rem.yaml.


### Optical files

#### OpticalProperties_OD.yaml
This is the simple optical property file to run with OD.yaml. It mostly uses the max values that are in the wavelength depend file.

#### OpticalProperties_OD_Rem.yaml
This is the optical property file to run with OD_Rem.yaml. It has three sets of reflectivity:  0, 40 and 98% to be used for the WST and OC.

#### OpticalProperties_ODFull.yaml
This holds the wavelength dependant optical properties for the OD. Currently not being used yet as Chroma needs to be updated to use them. Optical properties references and data [here](https://docs.google.com/spreadsheets/d/1iSRgq9s_rLq8sha7DRQ1lINoWqlFK5WYeVmT2nKZEEg/edit?usp=sharing).
