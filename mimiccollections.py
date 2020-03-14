from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstrac base class."""
    
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""
        
    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""
        
    def __contains__(self, val):
        """Return True if val found in the sequence, False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False
        
    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('value not in sequence')
        
    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
        
    def __eq__(self, other):
        """Return True if two sequences are equal, False otherwise."""
        if len(self) != len(other):
            return False
        else:
            for j in range(len(self)):
                if self[j] != other[j]:
                    return False
        return True
        
    def __lt__(self, other):
        """Return True if seq1 < seq2, False otherwise."""
        for j in range(min((len(self)), len(other))):
            if self[j] > other[j]:
                return False
        return True
        
        
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
        
        
class ReversedSequenceIterator:
    """An reversed iterator for any of Python's sequence types."""
    
    def  __init__(self, seq):
        """Create a reserved iterator for the given sequence."""
        self._seq = seq
        self._k = len(self._seq)
        
    def __next__(self):
        """Return the next element, or else raise StopIterator error."""
        self._k -= 1
        if self._k >= 0:
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
        
    def __contains__(self, val):
        """Return True if val found in the sequence, False otherwise."""
        return (val - self._start) % self._step == 0 and (val - self._start) // self._step in range(0, len(self))


    
    
