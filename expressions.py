class Exponentation():
    """Represent an exponentation of degree n"""
    
    def __init__(self, a=1, n=0):
        """
        Initilize a exponentation
        
        a           coefficient (default 1)
        n           exponent (default 0)
        """
        self._data = {'a': a, 'n': n}
        
    def __getitem__(self, j):
        """Return exponent, coefficient, current x value."""
        return self._data[j]
        
    def __setitem__(self, j, val):
        """Set exponent, coefficient or x with a given value."""
        self._data[j] = val
        
    def __add__(self, other):
        """Calculate sum of two exponetation of the same degree."""
        if not isinstance(other, Exponentation):
            raise TypeError
        return Exponentation(self['a'] + other['a'] , self._data['n']) if self['n'] == other['n'] else None
        
    def __radd__(self, other):
        return self + other
        
    def __mul__(self, other):
        """Multiple with a number or other exponentation."""
        if isinstance(other, (int, float, Exponentation)):
            if isinstance(other, (int, float)):
                other_new = Exponentation(other)
            else:
                other_new = Exponentation(other['a'], other['n'])
            return Exponentation(self['a'] * other_new['a'], self['n'] + other_new['n'])
        else:
            raise TypeError
            
    def __rmul__(self, other):
        return self * other
        
    def __neg__(self):
        """Return negative of a exponentation."""
        return self * (-1)
    
    def __sub__(self, other):
        """Return the difference between two exponentations."""
        return self + (-other)
        
    def __rsub__(self, other):
        return other - self
        
    def _reverse(self):
        """Return reverse of an exponentation."""
        if self['a'] == 0:
            raise ZeroDivisionError
        return Exponentation(1/self['a'], -self['n'])
    
    def __truediv__(self, other):
        """Return quotient of two exponentations."""
        return self * other._reverse()
        
    def __rtruediv__(self, other):
        return other * self._reverse()
        
    def _deriv(self, order=1):
        """Return derivative of an exponentation."""
        coef = self['a']
        for j in range(order):
            coef *= self['n'] - j
        return Exponentation(coef, self['n'] - order)
        
            
    def __str__(self):
        """Return string representation of exponentation."""
        coef = str(self._data['a']) if (abs(self._data['a']) != 1 or self._data['n'] == 0) else ('-' if self._data['a'] < 0 else '')
        exp  = '' if self._data['n'] == 0 or self._data['a'] == 0 else ('x' if self._data['n'] == 1 else 'x^' + (str(self._data['n']) if self._data['n'] > 0 else '(' + str(self._data['n']) + ')'))
        return coef + exp
        
        

class Polynomial:
    """Represent a polynomial of degree n."""
    
    def __init__(self, coefs):
        """
        Initialze a polynomial with given sequence coefficients.
        
        coefs       sequence of coefficient (eg. [2, 0, 3, 1] for 3th degree polynomial)
        """
        self._elements = [Exponentation(coefs[j], len(coefs) - 1 - j) for j in range(len(coefs))]
        self._deg = len(coefs) - 1
        
    def _deriv(self, order=1):
        """Return fisrt derivative of a polynomial."""
        return Polynomial([0]) if order > self._deg else Polynomial([self._elements[j]._deriv(order)['a'] for j in range(self._deg + 1 - order)])
        
    
    def __str__(self):
        """Return string representation of a polynomial."""
        parts = [str(element) for element in self._elements if element['a'] != 0 or self._deg == 0]
        for j in range(len(parts)):
            if parts[j][0] == '-':
                parts[j] = '(' + parts[j] + ')'
        return ' + '.join(parts)
        



