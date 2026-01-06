import random

def random_ai(game):
    moves = game.available_moves()
    return random.choice(moves) if moves else None
