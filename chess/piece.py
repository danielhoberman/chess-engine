from enum import IntEnum


class Piece(IntEnum):
    None_ = 0
    King = 1
    Pawn = 2
    Knight = 3
    Bishop = 4
    Rook = 5
    Queen = 6
    White = 8
    Black = 16

    @staticmethod
    def is_color(piece: int, color: "Piece") -> bool:
        """
        Returns True if the piece has the specified color.

        Args:
            piece: An integer representing the piece (type | color).
            color: Piece.White or Piece.Black

        Returns:
            bool
        """
        if piece == Piece.None_:
            return False
        return (piece & (Piece.White | Piece.Black)) == color

    @staticmethod
    def is_sliding_piece(piece: int) -> bool:
        """
        Returns True if the piece is a sliding piece (Bishop, Rook, or Queen).
        """
        return piece in (Piece.Bishop, Piece.Rook, Piece.Queen)
