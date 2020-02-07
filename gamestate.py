from copy import deepcopy


class GameState:

    def __init__(self, n, m):
        """The GameState class constructor performs required
        initializations when an instance is created. The class
        should:

        1) Keep track of which cells are open/closed
        2) Identify which player has initiative
        3) Record the current location of each player

        Parameters
        ----------
        self:
            instance methods automatically take "self" as an
            argument in python

        Returns
        -------
        None
        """
        self._m = m  # row
        self._n = n  # col
        self._cells = [[-1 for i in range(n)] for i in range(m)]
        self._cells[-1][-1] = 1  # block down right for y
        self._last_x = (0, 0)  # row, col
        self._last_y = (0, 0)
        self._initiative = 0  # 0 for x, 1 for y

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        available = []
        direction = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
        if sum(self._last_x) == 0:
            if self._initiative == 0:
                for i in range(self._m):
                    for j in range(self._n):
                        if i == 1:
                            continue
                        available.append((i, j))
        elif sum(self._last_y) == 0:
            if self._initiative == 1:
                for i in range(self._m):
                    for j in range(self._n):
                        if i == 0:
                            continue
                        available.append((i, j))
        else:
            if self._initiative == 1:
                _x, _y = self._last_y
                for i, j in direction:
                    while 0 <= _x + i < self._m and 0 <= _y + i < self._n:
                        if self._cells[_x][_y] == 1:
                            break
                        available.append((_x, _y))
            if self._initiative == 0:
                _x, _y = self._last_x
                for i, j in direction:
                    while 0 <= _x + i < self._m and 0 <= _y + i < self._n:
                        if self._cells[_x][_y] == 0:
                            break
                        available.append((_x, _y))
        return available

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
            (e.g., (0, 0) if the active player will move to the
            top-left corner of the board)
        """
        newSate = deepcopy(self)
        newSate._cells[move[0]][move[1]] = self._initiative
        if self._initiative:
            self._last_y = move
            self._initiative = 0
        else:
            self._last_x = move
            self._initiative = 1
        return newSate


if __name__ == "__main__":
    emptyState = GameState()  # create an instance of the object
