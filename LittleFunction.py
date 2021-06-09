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