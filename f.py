class Vector:
    """Represent a vector in a multidimensional space."""
    
    def __init__(self, d):
        """Create a d-dimensional vector of zeros."""
        self._coords = [0] * d
        
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
        
    def __eq__(self, other):
        """Return True if vectors have same coordinates"""
        return self._coords == other._coords
        
    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other
        
    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'
   
        
class SequenceIterator:
    """An iterator for any of Python's sequence types."""
    
    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence
        self._k = -1
        
    def __next__(self):
        """Return the next element, or else raise StopIterator error."""
        self._k += 1
        if self._k < len(self._seq):
            return self._seq[self._k]
        else:
            raise StopIteration()
            
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator"""
        return self
        
        
class Range:
    """A class that mimics the built-in range class."""
    
    def __init__(self, start, stop=None, step = 1):
        """
        Initialize a Range instance.
        
        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step cannot be 0')
            
        if stop is None:
            start, stop = 0, start
            
        self._length = max(0, (stop - start + step -1) // step)
        self._start = start
        self._step = step
        
    def __len__(self):
        """Return number of entries in the range."""
        return self._length
        
    def __getitem__(self, k):
        """Return entry at index k"""
        if k < 0:
            k += len(self)
            
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
            
        return self._start + k * self._step

















