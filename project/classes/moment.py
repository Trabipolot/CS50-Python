import numpy as np

class Moment:
    def __init__(self, M, pos_x, pos_z = 0, axes = "y") -> None:
        self.M = M
        self.pos_x = pos_x
        self.pos_z = pos_z
        self.axes = axes

    @property
    def M(self):
        return self._M

    @M.setter
    def M(self,value):
        if isinstance(value, (int, float)):
            self._M = value
        else:
            raise ValueError("M must be a number")
        
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
    def axes(self):
        return self._axes
    
    @axes.setter
    def axes(self,value):
        if value in ["x","y","z"]:
            self._axes = value
        else:
            raise ValueError("axes must be a x,y or z")
        
    
    
        