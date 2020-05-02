class TicTacToe:
    """Management of a Tic-Tac_toe game."""
    
    def __init__(self):
        """Start a new game."""
        self._board = [[' '] * 3 for j in range(3)]
        self._player = 'X'
        
    def mark(self, i, j):
        """Put an X or O mark at position (i, j) for next player's turn."""
        if not (0 <= i <= 2 and 0 <=j <= 2):
            raise IndexError
        if self._board[i][j] != ' ':
            raise IndexError('Position occupied')
        self._board[i][j] = self._player
        if self._player == 'X':
            self._player = 'O'
        else:
            self._player = 'X'
            
    def _is_win(self, mark):
        """Check whether the given player won."""
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])
                
    def winner(self):
        """Return mark of winning player."""
        for mark in 'XO':
            if self._is_win(mark):
                return mark
        return None
        
    def __str__(self):
        """Return string representation of current game board."""
        rows = [' | '.join(self._board[r]) for r in range(3)]
        return '\n---------\n'.join(rows)
        

if __name__ == '__main__':
    game = TicTacToe()
    game.mark(1, 2)
    print(game)
