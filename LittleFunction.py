import numpy as np
import matplotlib.pyplot as plt
import os

"""
Rename STL files the fusion saves to removed unneeded parts.
"""
def renameSTLs(path):
    print("Looking in " + path)
    
    for filename in os.listdir(path):
        if filename.endswith(".stl"): 
    #         print(filename)
            x = filename.split('_')

            if "WT" in filename:
                old = filename
                new = x[0] + "_" + x[5] + "_" + x[-1]
            elif "PMT" in filename:
                old = filename
                
                for j, l in enumerate(x):
                    split_space = l.split(' ')
                    if len(split_space) > 1:
                        l = ""
                        for word in split_space:
                            l = l + word
                        x[j] = l
                
                new = x[0] + "_" + x[3] + "_" + x[7] + "_" + x[-4] + x[-2] + "_" + x[-1]
    #             print(r"{}{}".format(path, new))
            else:
                old = filename
                new = x[0] + "_" + x[2] + x[3]

    #             print(r"{}{}".format(path, new))

            print("Rename {} to {}".format(old, new))
            os.rename(r"{}{}".format(path, old),r"{}{}".format(path, new))
            continue

        else:
            continue
            
"""
Prints out wavelenght dependant values for the Yaml file in nice format for given wavelength
bounds.
bounds = [lower, upper] limits of wavelength that should be printed
"""
def ListForYaml(wavelength, values, bounds=None):
    #sort the data so the wavelenghts are in increasing order
    inds = wavelength.argsort()
    wavelength = wavelength[inds]
    values = values[inds]

    if isinstance(bounds, list):
        #get the min and max index of the range of values we want if bounds are given
        minI = np.where(wavelength == np.min(wavelength[wavelength > bounds[0]]))[0][0]
        maxI = np.where(wavelength == np.max(wavelength[wavelength < bounds[1]]))[0][0]
        
#         print(minI, maxI)
        if minI==0 and maxI==len(wavelength):
            print('Using full data set')
        elif maxI==len(wavelength):
            wavelength = wavelength[minI:]
            values = values[minI:]
        else:                    
            wavelength = wavelength[minI:maxI+1]
            values = values[minI:maxI+1]
        
        if len(wavelength)==0:
            print("No data is in that range!")

    for i, wl in enumerate(wavelength):
            
        print("{}: !!python/tuple [{:.5},{:.5}]".format(i, wl, values[i]))
        
        
def getCherenkovWavelengthSample(NumPhotons, MuonEnergy, Interp=True):   
    ### Get Beta from muon###
    
    gamma = MuonEnergy/0.10566 #divide by the muon mass [0.10566 GeV]
    beta =  np.sqrt(1.0 - 1.0/(gamma**2.0)) #should be [.9, .99]
    
    '''
    #From Soud's code
    #In eV 
    energies = np.array([0.602, 0.689, 1.03,  1.926, 2.583, 2.845, 2.857, 3.124,3.457, 3.643, 3.812, 4.086, 4.511, 4.953, 5.474, 6.262, 7.000, 8.300, 10.00, 12.60])
    #Refractive index of water from Segelstein, David J. The complex refractive index of water. Diss. University of Missouri--Kansas City, 1981.
    n = np.array([1.303, 1.3120,   1.3239,   1.3313, 1.3358, 1.3376, 1.3376, 1.3392, 1.3423, 1.3442, 1.3460, 1.3486, 1.3540, 1.3619, 1.3723, 1.3960, 1.3960, 1.3960,1.3960, 1.3960])
    
    #Only take the ~near visible range (where photomultiplier tubes are sensitive). 
    #This is the tail of the Cherenkov emission spectrum.
    cut = [3,7] #there are only 4 data points here which isn't great
    energies=energies[cut[0]:cut[1]]
    n=n[cut[0]:cut[1]]
    '''
    
    #From nEXO_offline
    eV = 1
    energies = np.array([2.07, 2.09, 2.12, 2.20, 2.31, 2.41, 2.48, 2.55, 2.71, 2.83 ,
           2.96, 3.05, 3.13, 3.25, 3.32, 3.45, 3.57, 3.69, 3.85, 3.99, 4.26, 4.99, 5.29]) #eV

    n = np.array([1.332, 1.33233458, 1.33275974, 1.333, 1.33337057,1.33440426, 1.33497163, 
            1.33553901, 1.33667376, 1.33746809, 1.33824548, 1.33866779, 1.33926229, 1.34044132, 
            1.34115378, 1.3422317 , 1.34324954, 1.34459331, 1.34635211, 1.34761808, 1.35056125, 
            1.36267944, 1.36844391])
    #'''
    #get wavelengths and frequencies from the energy array
    wavelengths = 1239.8/energies
    freq = 3e17/wavelengths
    
    #calculate the energy lost per unit length from the Frank-Tamm Formula
    #assuming
    E_loss = 1.0/(4*np.pi) * freq*(1.0 - 1.0/(beta**2.0 * n**2.0))
    E_loss_rel = E_loss/np.abs(E_loss.sum()) #renormalize
    
    
    ### Second option with interpolation ###
    #interpolated - I think this is better
    wavelength_intep = np.linspace(np.min(wavelengths), np.max(wavelengths), 300)
    #need to flip data arrays as np.interp needs increasing x values
    E_loss_rel_intep = np.interp(wavelength_intep, wavelengths[::-1], E_loss_rel[::-1])

    E_loss_rel_intep = E_loss_rel_intep/np.sum(E_loss_rel_intep)
    
    if not Interp:
        photonWavelen = np.random.choice(wavelengths, p=E_loss_rel, size=NumPhotons)
    else:
        photonWavelen = np.random.choice(wavelength_intep, p=E_loss_rel_intep, size=NumPhotons)
    
    return photonWavelen