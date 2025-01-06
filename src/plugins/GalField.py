"""
galois field code from https://github.com/pmneila/Lights-Out/blob/master/lightsout.py
"""

class GaloisField2(object):
    def __init__(self, a=0):
        self.value = int(a) & 1
    
    def __add__(self, rhs):
        return GaloisField2(self.value + GaloisField2(rhs).value)
    
    def __mul__(self, rhs):
        return GaloisField2(self.value * GaloisField2(rhs).value)
    
    def __sub__(self, rhs):
        return GaloisField2(self.value - GaloisField2(rhs).value)
    
    def __truediv__(self, rhs):
        return GaloisField2(self.value / GaloisField2(rhs).value)
    
    def __repr__(self):
        return str(self.value)
    
    def __eq__(self, rhs):
        if isinstance(rhs, GaloisField2):
            return self.value == rhs.value
        return self.value == rhs
    
    def __le__(self, rhs):
        if isinstance(rhs, GaloisField2):
            return self.value <= rhs.value
        return self.value <= rhs
    
    def __lt__(self, rhs):
        if isinstance(rhs, GaloisField2):
            return self.value < rhs.value
        return self.value < rhs
    
    def __int__(self):
        return self.value
    
    def __long__(self):
        return self.value
    
