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



# class Board:
    
#     def __init__(self):
#         self.grid: list[list[Optional[ChessPiece]]] = [[None for _ in range(8)] for _ in range(8)]
#         self.board = self.setup_board()

#     def setup_board(self):
#         back_rank = [
#             Rook,
#             Knight,
#             Bishop,
#             Queen,
#             King,
#             Bishop,
#             Knight,
#             Rook
#         ]

#         # black back rank
#         for col, PieceClass in enumerate(back_rank):
#             self.grid[0][col] = PieceClass("black")

#         # black pawns
#         for col in range(8):
#             self.grid[1][col] = Pawn("black")

#         # white pawns
#         for col in range(8):
#             self.grid[6][col] = Pawn("white")

#         # white back rank
#         for col, PieceClass in enumerate(back_rank):
#             self.grid[7][col] = PieceClass("white")

#     def get_piece(self, position):
#         """Return the piece at (row, col)."""

#         row, col = position

#         return self.grid[row][col]
        

#     def move_piece(self, start, end):
#         """Move a piece from start to end if valid."""
#         pass

#     def print_board(self):
#         """Render the board to the console."""
#         print("  a b c d e f g h")
#         print(" -----------------")
#         for r in range(8):
#             print(f"{8 - r}|", end=" ")
#             for c in range(8):
#                 piece = self.grid[r][c]
#                 if piece:
#                     print(piece.symbol, end=" ")
#                 else:
#                     print(".", end=" ")
#             print(f"|{8 - r}")
#         print(" -----------------")
#         print("  a b c d e f g h")

#     def _in_bounds(self, position):
#         """Check if a piece is on the chess board"""

#         row, col = position
#         if 0 <= row < 8 and 0 <= col < 8:
#             return True
#         return False

#     def _is_empty(self, position):
#         """Does a piece exist at this position"""

#         row, col = position
#         return self.grid[row][col] is None
    

#     def _is_enemy(self, pos, color):
#         """
#         - Checks if the piece at pos belongs to the opposite color.
#         - Returns False if the square is empty."""

#         row, col = pos
#         piece = self.grid[row][col]
#         if piece is None:
#             return False
#         return piece.color != color
        
        
