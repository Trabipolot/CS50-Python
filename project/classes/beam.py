from bearing import Bearing
from force import Force
from moment import Moment
import numpy as np

class Beam:     
       
    def __init__(self, length: float, e: int = None, x_start = 0, weight = 0):
        self.length = length
        self.e = e
        self.x_start = x_start
        self.x_end = x_start + length
        self.q = weight * 9.81 / length
        self.m_max = (self.q * self.length ** 2) / 8
        self.bearings = []
        self.forces = []
        self.moments = []
    
    def add_bearing(self, pos_x, pos_z = 0, angle = 270, fx = False, fz = False, m = False):
        bearing = Bearing(pos_x, pos_z, angle, fx, fz, m)
        self.bearings.append(bearing)
        self.bearings.sort(key = lambda bearing: (bearing.pos_x, -bearing.pos_z))

    def add_force(self, F, pos_x, pos_z = 0, angle = 270):
        force = Force(F, pos_x, pos_z, angle)
        self.forces.append(force)
        self.forces.sort(key = lambda force: (force.pos_x, -force.pos_z))

    def add_moment(self, M, pos_x, pos_z = 0, axes = "y"):
        moment = Moment(M, pos_x, pos_z, axes)
        self.moments.append(moment)
        self.moments.sort(key = lambda moment: (moment.pos_x, -moment.pos_z))

    def statically_determinate(self): 
        ...

    def calculate_reactions(self):
        if self.bearings[1].fz:
            self.bearings[1].Fz = (self.forces[0].F * (-np.sin(self.forces[0].angle) * (self.forces[0].pos_x - self.bearings[0].pos_x))) / (self.bearings[1].pos_x - self.bearings[0].pos_x)
        if self.bearings[0].fz:
            self.bearings[0].Fz = (self.forces[0].F * (-np.sin(self.forces[0].angle) * (self.forces[0].pos_x - self.bearings[1].pos_x))) / (self.bearings[0].pos_x - self.bearings[1].pos_x)
        if self.bearings[1].fx:
            self.bearings[1].Fx = self.forces[0].F * (-np.cos(self.forces[0].angle))
        if self.bearings[0].fx:
            self.bearings[0].Fx = self.forces[0].F * (-np.cos(self.forces[0].angle))
        if np.isclose(self.bearings[0].Fz + self.bearings[1].Fz, self.forces[0].F * (-np.sin(self.forces[0].angle))):
            print("test Fz passed")
        else:
            raise ValueError("Your calculation of Fz does not output an equilibrium")
        if np.isclose(self.bearings[0].Fx + self.bearings[1].Fx, self.forces[0].F * (-np.cos(self.forces[0].angle))):
            print("test Fx passed")
        else:
            raise ValueError("Your calculation of Fx does not output an equilibrium")

# 

    
