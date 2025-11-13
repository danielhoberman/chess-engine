from .piece import Piece
from typing import List


class Board:
    def __init__(self):
        self._squares: List[int] = [Piece.None_] * 64
        self._color_to_move: Piece = Piece.White

    # ----------------- color_to_move property -----------------
    @property
    def color_to_move(self) -> Piece:
        """The color of the player whose turn it is to move (Piece.White or Piece.Black)."""
        return self._color_to_move

    @color_to_move.setter
    def color_to_move(self, value: Piece) -> None:
        """Set the player whose turn it is to move."""
        if value not in (Piece.White, Piece.Black):
            raise ValueError("color_to_move must be Piece.White or Piece.Black")
        self._color_to_move = value

    # ----------------- squares property -----------------
    @property
    def squares(self) -> List[int]:
        """Get the board squares (list of 64 integers representing pieces)."""
        return self._squares

    @squares.setter
    def squares(self, new_squares: List[int]) -> None:
        """Set the board squares; must be a list of 64 integers."""
        if not isinstance(new_squares, list):
            raise TypeError("squares must be a list of integers")
        if len(new_squares) != 64:
            raise ValueError("squares must have exactly 64 elements")
        if not all(isinstance(p, int) for p in new_squares):
            raise TypeError("all squares must be integers")
        self._squares = new_squares
