class Progression:
    """
    Iterator producing a generic progression
    
    Default iterator produces the whole numbers 0, 1, 2, ...
    """
    
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self._current = start
        
    def _advance(self):
        """
        Update self._current to a new value.
        
        This should be overidden by a subclass to customize progression.
        
        By convention, if current is set to None, this desinates the end of a finite progression.
        """
        
        self._current += 1
        
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        if self._current is None:       # our convention to end a progression
            raise StopIteration()
        else:
            answer = self._current
            self._advance()             # advance to prepare for next time
            return answer
    
    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self
        
    def print_progression(self, n):
        """Print next n values of the progression."""
        print(' '.join(str(round(next(self), 3)) for j in range(n)))


class ArithmeticProgression(Progression):
    """Iterator producing an arthmetic progression."""
    
    def __init__(self, increment=1, start=0):
        """
        Create a new arithmetic progression.
        
        increment   the fixed constant to add to each term (default 1)
        start       the first term of the progression (default 0)
        """
        super().__init__(start)
        self._increment = increment
        
    def _advance(self):
        """Update current value by adding the fixed increment."""
        self._current += self._increment
        
        
class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""
    
    def __init__(self, base=2, start=1):
        """
        Create a new geometric progression.
        
        base        the fixed constant multiplied to each term (default 2)
        start       the first term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base
        
    def _advance(self):
        """Update current value by multiplying it by the base value."""
        self._current *= self._base
        

class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    
    def __init__(self, first=0, second=1):
        """
        Create a new fibonacci progression.
        
        first       the first term of the progression (default 0)
        second      the second term of the progression (default 1)
        """
        super().__init__(first)
        self._prev = second - first
        
    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current


class DiffProgression(Progression):
    """Each value is the absolute value of the difference between the previous two values."""
    
    def __init__(self, first=2, second=200):
        """
        An element is the absolute value of difference between 2 previous elements.
        
        first       the first element of the progression (default 2)
        second      the second element of the progression (default 200)
        """
        super().__init__(first)
        self._prev = abs(first + second)
        
    def _advance(self):
        """Update the current value by absolute the difference between the 2 previous."""
        self._prev, self._current = self._current, int(abs(self._current - self._prev))

class SquareProgression(Progression):
    """Iterator producing a square root progression."""
    
    def __init__(self, start=65.536):
        """
        Create a new fibonacci progression.
        
        start       the first element of the progression (default 65.536)
        """
        super().__init__(start)
        
    def _advance(self):
        """Update the current value"""
        self._current = round(self._current ** (1/2), 3)
































