import numpy as np

class Force:
    def __init__(self, F: float, pos_x: float, pos_z: float = 0, angle: float = 90):
        self.F = F
        self.pos_x = pos_x
        self.pos_z = pos_z
        self.angle = angle

    @property
    def F(self):
        return self._F
    
    @ F.setter
    def F(self,value):
        if isinstance(value,(int, float)) and value >= 0:
            self._F = value
        else:
            raise ValueError("Force must be a positive number")
        
    @property
    def pos_x(self):
        return self._pos_x
    
    @pos_x.setter
    def pos_x(self,value):
        if isinstance(value, (int, float)):
            self._pos_x = value
        else:
            raise ValueError("pos_x must be a number")
        

    @property
    def pos_z(self):
        return self._pos_z
    
    @pos_z.setter
    def pos_z(self,value):
        if isinstance(value, (int, float)):
            self._pos_z = value
        else:
            raise ValueError("pos_z must be a number")
    
    @property
    def angle(self):
        return self._angle
    
    @angle.setter
    def angle(self,value):
        if isinstance(value, (int, float)) and 0 <= value < 360:
            self._angle = np.radians(value)
        else:
            raise ValueError("angle must be a number between 0 and 359")
        
    

    