from .piece import Piece

class Board:
    def __init__(self):
        self.squares = [0] * 64
        self._color_to_move = Piece.White

    @property
    def color_to_move(self) -> Piece:
        """The color of the player whose turn it is to move (Piece.White or Piece.Black)."""
        return self._color_to_move

    @color_to_move.setter
    def color_to_move(self, value: int) -> None:
        """Set the player whose turn it is to move."""
        if value not in (Piece.White, Piece.Black):
            raise ValueError("color_to_move must be Piece.White or Piece.Black")
        self._color_to_move = value
        
