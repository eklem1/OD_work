# OD - nEXO's Outer Detector 

These files are all for running simulations of the photons produced by muons passing through nEXO's water tank, or outer detector. All relenvant geometry files can be found in  [~/Geometry/OD/](https://github.com/nEXO-collaboration/chroma-simulation/tree/eklem1/issue_6/Geometry/OD) and it's subfolders.

### Detector files
These files set up the geometry, point to the required locations for the imported stl files, where the data is saved and much more. They also specify what generator is used to create photons. 

The CherenkovSimple Generator should be used to generate photons from a single muon's path.
```
Simulation:                      
  Generator: CherenkovSimple; [0,-1,-1]; 200  #type of Generator; 'muon' momentum; length of muon track in mm
  NumberOfPhotons: 200                        # number of photons per event - really you should set it to 10*(length of muon track) as Cherenkov light should generate ~10 photons/mm in water
  NumberOfSources: 1                          # number of events 
  NumberOfRuns: 1                             # number of runs define how often NumberOfPhotons x NumberOfSources will be simulated
  PhotonLocation:  Point=0,0,-3400            #Define start position of muon track
```


#### OD.yaml
This file should run the most updated version of the full OD simulation.

#### OD_Rem.yaml
This file sets up to run a simulation with a simplified geometry to replicate Remington's work (found at:). The PMTs here are simple half hemispheres and it uses the simplified optical properties found in OpticalProperties_OD_Rem.yaml.

### Optical files

#### OpticalProperties_OD.yaml

#### OpticalProperties_OD_Rem.yaml

#### OpticalProperties_ODFull.yaml
This holds the wavelength dependant optical properties for the OD.
