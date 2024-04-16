from beam import Beam

class BeamRectangular(Beam):
    def __init__(self, length, height, width, e = None, x_start = 0):
        super().__init__(length, e, x_start)
        self.height = height
        self.width = width
        self.Iy = (self.width * self.height ** 3) / 12
        self.Iz = (self.height * self.width ** 3) / 12
        self.Ix = (self.length * self.height ** 3) / 12