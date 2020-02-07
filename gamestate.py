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
        self._cells = [[0 for i in range(n)] for i in range(m)]
        self._cells[-1][-1] = 1  # block down right for y
        self._last_x = (0, 0)
        self._last_y = (0, 0)
        self._initiative = 0  # 0 for x, 1 for y



if __name__ == "__main__":
    emptyState = GameState()  # create an instance of the object
