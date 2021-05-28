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

    if isinstance(bounds, list):
        wavelength = wavelength[(wavelength > bounds[0]) & (bounds[1]>wavelength)]

    for i, wl in enumerate(wavelength):
            
        print("{}: !!python/tuple [{:.5},{:.5}]".format(i, wl, values[i]))