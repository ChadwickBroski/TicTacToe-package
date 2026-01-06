# TicTacToe package

A clean and efficient Tic Tac Toe engine.

## Usage
```python
from tictactoe import TicTacToe, random_ai

game = TicTacToe()

game.make_move(0)
game.make_move(random_ai(game))

print(game.board)
print(game.winner)

