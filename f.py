class Vector:
    """Represent a vector in a multidimensional space."""
    
    def __init__(self, data):
        """
        Create a vector given by data.
        
        If data is a number, create a data-dimensional vector.
        If data is a sequence, take it as coordinates.
        """
        if isinstance(data, int):
            if data <= 0:
                raise ValueError('dimension must be positive')
            self._coords = [0] * data
        elif isinstance(data, (list, tuple)):
            self._coords = list(data)
        else:
            raise TypeError('parameter must be a number or sequence')
            
        
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)
        
    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]
        
    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val
        
    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimension must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
        
    def __sub__(self, other):
        """Return difference between two vectors."""
        if len(self) != len(other):
            raise ValueError('dimension must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
        
    def __neg__(self):
        """Return opposite of vector."""
        return Vector(len(self)) - self
        
    def __radd__(self, other):
        """Return sum of two vector."""
        return self + other
        
    def __rsub__(self, other):
        """Return difference between two vectors."""
        return -self + other
        
        
    def __mul__(self, other):
        """Return product by a vector with a number."""
        if isinstance(other, (int, float)):
            return [i * other for i in self]
        else:
            if len(self) != len(other):
                raise ValueError('dimension must agree')
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
            return result
        
        
    def __rmul__(self, number):
        """Return product by a vector with a number."""
        return self * number
        
        
    def __eq__(self, other):
        """Return True if vectors have same coordinates"""
        return self._coords == other._coords
        
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
        
    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'
           
        
















