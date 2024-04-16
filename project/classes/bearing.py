import numpy as np

class Bearing:
    def __init__(self,  pos_x: float, pos_z: float = 0, angle: float = 270, fx: bool = False, fz: bool = False, m: bool = False):
        self.pos_x = pos_x
        self.pos_z = pos_z
        self.angle = angle
        self.fx = fx
        self.fz = fz
        self.m = m
        if self.fz:
            self.Fz = None
        else:
            self._Fz = 0
        if self.fx:
            self.Fx = None
        else:
            self._Fx = 0
        if self.m:
            self.M = None
        else:
            self._M = 0

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
    
    @property
    def fx(self):
        return self._fx
    
    @fx.setter
    def fx(self,value):
        if isinstance(value, (bool)):
            self._fx = value
        else:
            raise ValueError("fx must be bool")
        
    @property
    def fz(self):
        return self._fz
    
    @fz.setter
    def fz(self,value):
        if isinstance(value, (bool)):
            self._fz = value
        else:
            raise ValueError("fz must be bool")
    
    @property
    def m(self):
        return self._m
    
    @m.setter
    def m(self,value):
        if isinstance(value, (bool)):
            self._m = value
        else:
            raise ValueError("m must be bool")
        
    @property
    def Fx(self):
        return self._Fx

    @Fx.setter
    def Fx(self, value):
        if self.fx:
            if value is None or isinstance(value, (int, float)):
                self._Fx = value
            else:
                raise ValueError("Fx must be a number or None")
        else:
            raise AttributeError("Fx cannot be set unless fx is True")
        
    @property
    def Fz(self):
        return self._Fz

    @Fz.setter
    def Fz(self, value):
        if self.fz:
            if value is None or isinstance(value, (int, float)):
                self._Fz = value
            else:
                raise ValueError("Fz must be a number or None")
        else:
            raise AttributeError("Fz cannot be set unless fz is True")
        
    @property
    def M(self):
        return self._M

    @M.setter
    def M(self, value):
        if self.m:
            if value is None or isinstance(value, (int, float)):
                self._M = value
            else:
                raise ValueError("M must be a number or None")
        else:
            raise AttributeError("M cannot be set unless m is True")
        
    


    
