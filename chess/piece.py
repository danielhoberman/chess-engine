
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


# class ChessPiece:
#     def __init__(self, color, piece_type, symbol):
#         self.color = color
#         self.piece_type = piece_type
#         self.symbol = symbol


# class Pawn(ChessPiece):
#     def __init__(self, color):
#         symbol = "p" if color == "black" else "P"
#         super().__init__(color, "pawn", symbol)

#     def valid_moves(self, board, position):
#         """
#         Pawn movement:
#         - forward one square (must be empty)
#         - forward two squares from starting rank
#         - diagonal capture
#         - later: en passant, promotion
#         """
#         # row, col = position
#         # moves = []

#         # direction = -1 if self.color == "white" else 1
#         # start_row = 6 if self.color == "white" else 1

#         pass



# class Knight(ChessPiece):
#     def __init__(self, color):
#         symbol = "n" if color == "black" else "N"
#         super().__init__(color, "knight", symbol)

#     def valid_moves(self, board, position):
#         """
#         Knight movement:
#         - L-shape: (±2, ±1) or (±1, ±2)
#         - can jump over pieces
#         """
#         # row, col = position
#         # moves = []

#         # knight_offsets = [
#         #     (2, 1), (2, -1), (-2, 1), (-2, -1),
#         #     (1, 2), (1, -2), (-1, 2), (-1, -2)
#         # ]

#         pass

# class Bishop(ChessPiece):
#     def __init__(self, color):
#         symbol = "b" if color == "black" else "B"
#         super().__init__(color, "bishop", symbol)

#     def valid_moves(self, board, position):
#         """
#         Bishop movement:
#         - diagonal sliding in 4 directions
#         - stops when encountering a piece
#         """
#         # row, col = position
#         # moves = []

#         # directions = [(1,1), (1,-1), (-1,1), (-1,-1)]

#         pass



# class Rook(ChessPiece):
#     def __init__(self, color):
#         symbol = "r" if color == "black" else "R"
#         super().__init__(color, "rook", symbol)

#     def valid_moves(self, board, position):
#         """
#         Rook movement:
#         - horizontal and vertical sliding
#         - stops on pieces
#         """
#         # row, col = position
#         # moves = []

#         # directions = [(1,0), (-1,0), (0,1), (0,-1)]

#         pass


# class Queen(ChessPiece):
#     def __init__(self, color):
#         symbol = "q" if color == "black" else "Q"
#         super().__init__(color, "queen", symbol)

#     def valid_moves(self, board, position):
#         """
#         Queen movement:
#         - rook + bishop combined
#         - 8 sliding directions
#         """
#         # row, col = position
#         # moves = []

#         # directions = [
#         #     (1,0), (-1,0), (0,1), (0,-1),
#         #     (1,1), (1,-1), (-1,1), (-1,-1)
#         # ]

#         pass


# class King(ChessPiece):
#     def __init__(self, color):
#         symbol = "k" if color == "black" else "K"
#         super().__init__(color, "king", symbol)

#     def valid_moves(self, board, position):
#         """
#         King movement:
#         - one square in any direction
#         - castling (later)
#         """
#         # row, col = position
#         # moves = []

#         # directions = [
#         #     (1,0), (-1,0), (0,1), (0,-1),
#         #     (1,1), (1,-1), (-1,1), (-1,-1)
#         # ]

#         pass








    





