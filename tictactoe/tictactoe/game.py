class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.current = "X"
        self.winner = None

    def make_move(self, index):
        if self.board[index] != " " or self.winner:
            return False

        self.board[index] = self.current
        self._check_winner()

        self.current = "O" if self.current == "X" else "X"
        return True

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v == " "]

    def is_draw(self):
        return " " not in self.board and self.winner is None

    def reset(self):
        self.__init__()

    def _check_winner(self):
        wins = (
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        )

        for a, b, c in wins:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                self.winner = self.board[a]
                return
