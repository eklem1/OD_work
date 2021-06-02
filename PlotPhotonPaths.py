"""
Reads in data from text file produced from running the chroma simulation
with PropagationMode: Steps and plots the photon's saved positions as they travel, 
along with renditions of some of the geometry files.

Note this code is currently indended to be edited in the code itself and may require
you to manually change the paths to the geometry files wanted. So for now all it takes to run is:  python Analysis/PlotPhotonPaths.py

REQUIRES: numpy-stl installed to be able to import and graph the stl files.
    Can be installed with: pip install numpy-stl
    For more information see: https://pypi.org/project/numpy-stl/
"""
import numpy as np 
import matplotlib.pyplot as plt 
from stl import mesh
from mpl_toolkits import mplot3d

ChromaPath = '/home/eklem/chromasim/chroma-simulation/'
GeoPath = ChromaPath + 'Geometry/OD/OD_withTestPMT/'

ChromaPath = './'
GeoPath = ChromaPath + 'CAD/'

"""
Reads in data from text file produced from running the chroma simulation
with PropagationMode: Steps. Saving the photon positions as well as the shift
in the geometry used in chroma.
"""
def readPhotonPaths(filename):

    f = open(filename, "r")
    paths1 = [[],[],[]]
    paths = []
    save = -1

    lst = f.read().splitlines()
    f.close()

    num_lines = len(lst)
    
    #get the geometry shift - should be the 3rd line down
    centerSh = [float(x) for x in lst[2].split(', ')[:-1]]
    print("Shifting geometry by: ", centerSh)

    for i in range(5, num_lines, 4):

        X = [float(x) for x in lst[i+1].split(', ')[:-1]]
        Y = [float(x) for x in lst[i+2].split(', ')[:-1]]
        Z = [float(x) for x in lst[i+3].split(', ')[:-1]]

        paths.append([X, Y, Z])
    return paths, centerSh

############# STL files for plotting #############

#watertank
WT_mesh = mesh.Mesh.from_file(GeoPath+'ODModel_SimulationModelUpdatedCryostat v14_simplified_WT_1_WaterTank_simplified_WT.stl')
WT_mesh.rotate([-1, 0.0, 0.0], np.radians(90))

#outer cyrostat
OC_mesh = mesh.Mesh.from_file(GeoPath+'ODModel_OuterCyrostat.stl')
OC_mesh.rotate([-1, 0.0, 0.0], np.radians(90))

#PMT glass surface
PMT_mesh = mesh.Mesh.from_file(GeoPath+'ODModel_PMT_Glassware_Component2Body1_Component2.stl')
PMT_mesh.rotate([-1, 0.0, 0.0], np.radians(90))

#PMT Steel connecting parts
PMT1_mesh = mesh.Mesh.from_file(GeoPath+'ODModel_PMT_MetalConnection_Component3Body1_Component3.stl')
PMT2_mesh = mesh.Mesh.from_file(GeoPath+'ODModel_PMT_MetalConnection_Component4Body1_Component4.stl')
PMTcon_mesh = mesh.Mesh(np.concatenate([m.data for m in [PMT1_mesh, PMT2_mesh]] ))
PMTcon_mesh.rotate([-1, 0.0, 0.0], np.radians(90))


listofParts = [WT_mesh, OC_mesh, PMT_mesh, PMTcon_mesh]
colors = ['black', 'black', 'darkred', 'blue']
alpha = [0.05, 0.1, 0.1, 0.1]
facecolor = [None, 'yellow', "red", None]

"""
Function to graph only wanted part of the geometry, with placement and coloring 
already configured.

parts - list of parts to graph, default is 'all' which graphs all parts, otherwise choose out
    of: ['WT', 'OC', 'PMTGlass', 'PMTconnect']
"""
def addGeometry(ax, parts='all'):
    
    if parts=='all':
        plotPart = np.arange(len(listofParts))
    else:
        plotPart = []
        for p in parts:
            if p=='WT':
                plotPart.append(0)
            elif p=='OC':
                plotPart.append(1)
            elif p=='PMTGlass':
                plotPart.append(2)
            elif p=='PMTconnect':
                plotPart.append(3)
#             elif p=='support': #can add more parts later
#                 plotPart.append(4)
                
    for i in plotPart:
            
        geometryPart = mplot3d.art3d.Line3DCollection(listofParts[i].vectors, linewidths=0.2, alpha=alpha[i])
        geometryPart.set_edgecolor(colors[0])
        geometryPart.set_facecolor(facecolor[i])
        ax.add_collection3d(geometryPart)

##################### Main #####################

#file to read from
paths, centerShift = readPhotonPaths(ChromaPath + 'photonPath.txt')

#Actually shifting over all the meshes
for part in listofParts:
    part.x += centerShift[0]
    part.y += centerShift[2]
    part.z += centerShift[1]

#configure 3D plot
fig = plt.figure(figsize=(7,7))
axes = mplot3d.Axes3D(fig)

for i in range(len(paths)): #you can limit how many photon paths are plotted here
    direction = np.arange(len(paths[i][0]))

    axes.plot3D(paths[i][0], paths[i][1], paths[i][2], 'blue', alpha=0.4) #plots lines as photon paths
    p = axes.scatter3D(paths[i][0], paths[i][1], paths[i][2], c=direction, cmap='viridis') #plots actual data points with color scale
    
    #print(paths[i][0][1], paths[i][1][1], paths[i][2][1])    
    
#use function to set what geometry should be used
addGeometry(axes, parts=['PMTconnect', 'PMTGlass'])#, 'OC']) 

#set axis limits
#axes.set_xlim3d(-6000, 6000)
#axes.set_ylim3d(-6000, 6000)
#axes.set_zlim3d(-6800, +6730)

# zoomed in example
axes.set_xlim3d(-1000, 1000)
axes.set_ylim3d(-1000, 1000)
axes.set_zlim3d(-7800, -6730)

axes.set_xlabel("X [mm]")
axes.set_ylabel("Y [mm]")
axes.set_zlabel("Z [mm]")
axes.xaxis.labelpad=20
axes.yaxis.labelpad=15

#helps see which way the photons are moving
fig.colorbar(p, label="Step Number", shrink=0.8)

#change angle of view - (elevation, azimuth) angles in degrees
# 'elev' stores the elevation angle in the z plane. 'azim' stores the azimuth angle in the x,y plane.
axes.view_init(0, 45)

# 0, 90 - XZ plane; 90, 90 - top view

#save the graph as a jpg
saveFile = 'PhotonPaths.jpg'
plt.savefig(saveFile)
print("Graph saved to: "+saveFile)

#show the graph
plt.show()
