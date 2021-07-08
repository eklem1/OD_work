'''
Generator: CherenkovSimple; axis-direction; length; momentum?

- position is set from PhotonLocation: , lets make this the muon's 'starting position'

'''

elif 'CherenkovSimple' in Generator:
        if ';' in Generator:
            Momentum = Generator.split(';')[1]
            Momentum = GetAxis(Momentum) #just stick with along an axis for now
            Length = Generator.split(';')[2] #length in mm

        Wavelength = 400 #nm
        
        Photons = CherenkovSimple(NPhotons, Wavelength, Position, Momentum, Length)


########################

def get_perp(x):
    """Returns an arbitrary vector perpendicular to `x`."""
    a = np.zeros(3)
    a[np.argmin(abs(x))] = 1
    return np.cross(a,x)


def CherenkovSimple(NPhotons, Wavelength, Position, Momentum, Length):

    parentMomentum = np.array([Momentum[0], Momentum[1], Momentum[2]])

    parentMomentumUnit = parentMomentum/np.linalg.norm(parentMomentum) 
    #so we assume the distance is set by the Length, and should use parentMomentumUnit
    # to calculate any distances traveled
    
    parentEntryPosition =  np.array([Position[0], Position[1], Position[2]])
    
    parentEndPosition = Length*parentMomentumUnit + parentEntryPosition
        
    dx, dy, dz = parentEndPosition - parentEntryPosition
    
    #print(parentEntryPosition)
    #print(parentEndPosition)
    
    photonsPerCm=100 #this is set by the physics in the Frank-Tamm formula
    '''
    you may want this number to fluctuate around ~100 and not be exactly 100 per cm, which would make 
    it more realistic. However, for long track lengths, I'm not sure if it makes too much of a difference
    '''

    #radians, approx Cherenkov angle in optical (~0.5 degree precision)
    thetaRel = 0.733 
    
    NPhotons = int(Length*photonsPerCm)
    
    photonsPosition = np.zeros((NPhotons, 3))
    photonsDirection = np.zeros((NPhotons, 3))

    #photons=np.zeros(NPhotons)

    #Soud used prange: 'Numba implements the ability to run loops in parallel'
    for i in range(NPhotons):
        
        numStepsAway = np.random.rand()*Length #pick a random point on the track
        
        #photon position
        photonsPosition[i][0] = parentEntryPosition[0]+numStepsAway*parentMomentumUnit[0]
        photonsPosition[i][1] = parentEntryPosition[1]+numStepsAway*parentMomentumUnit[1]
        photonsPosition[i][2] = parentEntryPosition[2]+numStepsAway*parentMomentumUnit[2]

        #First, rotate relative to z axis by Cherenkov angle
        c, s = np.cos(thetaRel), np.sin(thetaRel) #cos and sine
        
        #this finds a vector perpendicular to the parentMomentum one (unless parentMomentum==[0.,0.,1.0])
        ux, uy, uz = get_perp(parentMomentumUnit)
    
        R = np.array([[c+ux*ux*(1.0-c), ux*uy*(1-c) - uz*s, ux*uz*(1-c) + uy*s], [uy*ux*(1-c)+uz*s, c+uy*uy *(1-c), \
                uy*uz*(1-c)-ux*s], [uz*ux*(1-c) - uy*s, uz*uy*(1-c)+ux*s, c+uz*uz * (1-c) ]])#rotation matrix

        momentum = R.dot(parentMomentum)
        
        #Now rotate random amount of phi about axis of parent trajectory
        phi=np.random.sample()*np.pi*2.0
        c, s = np.cos(phi), np.sin(phi) #cos and sine
        ux, uy, uz = parentMomentum[0], parentMomentum[1], parentMomentum[2]
        R = np.array([[c+ux*ux*(1.0-c), ux*uy*(1-c) - uz*s, ux*uz*(1-c) + uy*s], [uy*ux*(1-c)+uz*s, c+uy*uy *(1-c), uy*uz*(1-c)-ux*s], [uz*ux*(1-c) - uy*s, uz*uy*(1-c)+ux*s, c+uz*uz * (1-c) ]])#rotation matrix
        momentum = R.dot(momentum)
        
        #Photon momentum set so now leave track in a cherenkov cone 

        photonsDirection[i] = momentum/np.linalg.norm(momentum)
        
        #can get energy and therefore wavelength from momentum now here?

    Position = photonsPosition
    Direction = photonsDirection

    Wavelengths = np.repeat(Wavelength,NPhotons)
    Polarization = np.cross(Direction,uniform_sphere(NPhotons))

    return Photons(Position,Direction,Polarization,Wavelengths)




if

    Generator = self.Yaml['Simulation']['Generator']

    if ';' in Generator and 'CherenkovSimple' in Generator:
        Momentum = Generator.split(';')[1]
        Momentum = Momentum.split('[')[1].split(']')[0]
        Momentum = np.array([float(i) for i in Momentum.split(',')])#get x,y,z coords in an array

        Length = float(Generator.split(';')[2]) #length in mm
    else:
        print('For Cherenkov light the generator must be set to CherenkovSimple.')
        sys.exit()

    parentMomentum = np.array([Momentum[0], Momentum[1], Momentum[2]])

    parentMomentumUnit = parentMomentum/np.linalg.norm(parentMomentum) 
    #so we assume the distance is set by the Length, and should use parentMomentumUnit
    # to calculate any distances traveled
    
    parentEndPosition = Length*parentMomentumUnit + parentEntryPosition
    
    photonsPerMm= 10 #this is set by the physics in the Frank-Tamm formula
    '''
    you may want this number to fluctuate around ~100 and not be exactly 100 per cm, which would make 
    it more realistic. However, for long track lengths, I'm not sure if it makes too much of a difference
    '''

    #radians, approx Cherenkov angle in optical (~0.5 degree precision)
    thetaRel = 0.733 
    
    CNumPhotons = int(Length*photonsPerMm)

    photonsPosition = np.zeros((CNumPhotons, 3))
    photonsDirection = np.zeros((CNumPhotons, 3))

    for i in range(CNumPhotons):
        
        numStepsAway = np.random.rand()*Length #pick a random point on the track
        
        #photon position
        photonsPosition[i][0] = parentEntryPosition[0]+numStepsAway*parentMomentumUnit[0]
        photonsPosition[i][1] = parentEntryPosition[1]+numStepsAway*parentMomentumUnit[1]
        photonsPosition[i][2] = parentEntryPosition[2]+numStepsAway*parentMomentumUnit[2]
        
        #print(photonsPosition)
        #First, rotate relative to z axis by Cherenkov angle
        c, s = np.cos(thetaRel), np.sin(thetaRel) #cos and sine
        
        #this finds a vector perpendicular to the parentMomentum one (unless parentMomentum==[0.,0.,1.0])
        ux, uy, uz = get_perp(parentMomentumUnit)
    
        R = np.array([[c+ux*ux*(1.0-c), ux*uy*(1-c) - uz*s, ux*uz*(1-c) + uy*s], [uy*ux*(1-c)+uz*s, c+uy*uy *(1-c), \
                uy*uz*(1-c)-ux*s], [uz*ux*(1-c) - uy*s, uz*uy*(1-c)+ux*s, c+uz*uz * (1-c) ]])#rotation matrix

        momentum = R.dot(parentMomentum)
        
        #Now rotate random amount of phi about axis of parent trajectory
        phi=np.random.sample()*np.pi*2.0
        c, s = np.cos(phi), np.sin(phi) #cos and sine
        ux, uy, uz = parentMomentum[0], parentMomentum[1], parentMomentum[2]
        R = np.array([[c+ux*ux*(1.0-c), ux*uy*(1-c) - uz*s, ux*uz*(1-c) + uy*s], [uy*ux*(1-c)+uz*s, c+uy*uy *(1-c), \
                uy*uz*(1-c)-ux*s], [uz*ux*(1-c) - uy*s, uz*uy*(1-c)+ux*s, c+uz*uz * (1-c) ]])#rotation matrix
        momentum = R.dot(momentum)
        
        #Photon momentum set so now leave track in a cherenkov cone 

        photonsDirection[i] = momentum/np.linalg.norm(momentum)
        
        #can get energy and therefore wavelength from momentum now here?

    Position = photonsPosition
    Direction = photonsDirection