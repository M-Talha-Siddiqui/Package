import numpy as np


class Point:
    """Class representing a point."""

    def __init__(self, point):
        self._p = np.array(point)

    def __repr__(self):
        return f"Point({self._p})"

    def __sub__(self,other):
        # a - b
        # self - other

        #if other thing is a point,
        #we want to get a vector after subtration
        if isinstance(other, Point):
            return Vector(self._p - other._p)
        
        if isinstance(self , Vector):
            return Vector(self._p - other._v)
        
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._p +other._v)
        return NotImplemented



class Vector:
    """ Class representing a Vector."""

    def __init__(self,v):
        self._v  = np.array(v)
    
    def norm(self):
        """Return the norm of the vector"""
        return np.linalg.norm(self._v)

    def __repr__(self):
        return f"Vector({self._v})"

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self._v - other._v) 



if __name__ == "__main__":
    p1 = Point((1, 0, 0))
    p2 = Vector((0, 2, 0))

    print(p1 - p2)
#   difference = p1 - p2
#    print(difference)
#    print(difference.norm())
# c = Point.__sub__(self =b,other=a) should be of same type
#c= Point.__rsub__(self=a,other=b) can be ofdifferent type