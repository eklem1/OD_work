'''
Generator: CherenkovSimple; axis-direction; length; momentum?

- position is set from PhotonLocation: , lets make this the muon's 'starting position'

'''

elif 'CherenkovSimple' in Generator:
        if ';' in Generator:
            Direction = Generator.split(';')[1]
            Direction = GetAxis(Direction) #just stick with along an axis for now
            Length = Generator.split(';')[2] #length in mm

            Momentum = Generator.split(';')[3] #more here


        Photons = CherenkovSimple(NPhotons, Wavelength, Position, Direction, Length, Momentum)


########################


def CherenkovSimple(NPhotons, Wavelength, Position, Direction, Length, Momentum):
    Position = np.tile(Position, (NPhotons,1))

    Direction = np.tile(Direction, (NPhotons,1))

    Wavelengths = np.repeat(Wavelength,NPhotons)

    
    Polarization = np.cross(Direction,uniform_sphere(NPhotons))

    return Photons(Position,Direction,Polarization,Wavelengths)