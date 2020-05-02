class Frequencies:
    """Calculate frequency."""
    
    def __init__(self, data):
        """Calaculate frequency based on a dictionary."""
        self._data = data
        self._total = self._get_total()
        self._result = self._result()
        
    def __getitem__(self, key):
        """Get information about specified items in given data."""
        return self._data.get(key, 0)
        
    def _get_total(self):
        """Return total figure of the given data."""
        total = 0
        for key in self._data:
            total += self._data[key]
        return total
        
    def _get_frequency(self, key):
        """Return frequency of the specified item."""
        return round(self._data[key] / self._total * 100, 1)
        
    def _result(self):
        """Return frequencies of all items in given data."""
        result = {}
        for key in self._data.keys():
            result.update({key: self._get_frequency(key)})
        return result
        
    def _get_result(self):
        """Return result of the calculation."""
        return self._result
        
        
class Graph:
    """Visualize data with graph."""
    
    def __init__(self, figures):
        """Draw a ba graph with given data."""
        self._figures = figures
        self._freq = Frequencies(figures)
        self._data = self._freq._get_result()
        self._graph()
        
    def _len_x(self):
        """Return the len of x axis."""
        return 80
        
    def _indent(self):
        """Return the longest key of the given data."""
        return max(max([len(key) for key in self._data.keys()]) + 1, self._len_x()//20)
        
    def _graph_item(self, key):
        """Print graph of the given item."""
        return key.rjust(self._indent() - 1) + ' |' + ''.join('_' for j in range(round(self._len_x() * self._data[key] / 100) - 1)) + '.' + str(self._figures[key]) + ' (' + str(self._data[key]) + '%)'
    
    def _reorder(self):
        """Reorder key of items in data in order of decresing frequency."""
        keys = [key for key in self._data]
        keys.sort()
        keys.sort(key=self._freq._get_frequency)
        return keys
    
    def _graph(self):
        """Graph of data."""
        
        print(''.join([' ' for j in range(self._indent())]), '^', sep='')
        print(''.join([' ' for j in range(self._indent())]), '|', sep='')
        for key in self._reorder():
            print(self._graph_item(key))
        print(''.join([' ' for j in range(self._indent())]), '|', ''.join([''.join(['_' for k in range(int(self._len_x()/10 - 1))]) + '.' for i in range(10)]), str(self._freq._get_total()), sep='')
        print(''.join([' ' for j in range(self._indent() - self._len_x()//20)]), ''.join([str(j).center(self._len_x()//10) for j in range(0, 101, 10)]), sep='')

def val_of(data):
    return 
        
def get_characters(filename):
    string = open(filename, 'r').read()
    alphabet = {}
    for character in string:
        if 65 <= ord(character) <= 90 or 97 <= ord(character) <= 122:
            alphabet[character.lower()] = alphabet.get(character.lower(), 0) + 1
    return alphabet

Graph(get_characters("text.txt"))
        
