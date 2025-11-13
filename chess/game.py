from .board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = "white"
        self.move_history = []

    def make_move(self, notation):
        """Parse notation, validate the move, and update game state."""
        pass

    def switch_turn(self):
        self.current_turn = "black" if self.current_turn == "white" else "white"

    def is_check(self, color):
        pass

    def is_checkmate(self, color):
        pass

    def is_stalemate(self, color):
        pass
