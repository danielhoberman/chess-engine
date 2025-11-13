from dataclasses import dataclass
from typing import List
from .piece import Piece
from .board import Board
from .utils import DIRECTION_OFFSETS  # precomputed

@dataclass(frozen=True)
class Move:
    start_square: int
    target_square: int


class MoveGenerator:
    def __init__(self, board, edge_data):
        """
        Initialize the MoveGenerator.

        Args:
            board: Board instance containing the squares and color_to_move.
            edge_data: precomputed num_squares_to_edge (default imported globally).
        """
        self.board: 'Board' = board
        self.num_squares_to_edge = edge_data

    def generate_moves(self) -> List[Move]:
        """
        Generate all legal moves for the player whose turn it is.
        Currently handles sliding pieces (Bishop, Rook, Queen).
        """
        moves: List[Move] = []

        for start_square in range(64):
            piece: int = self.board.squares[start_square]
            if piece == Piece.None_:
                continue

            if not Piece.is_color(piece, self.board.color_to_move):
                continue

            if Piece.is_sliding_piece(piece):
                self._generate_sliding_moves(start_square, piece, moves)

            # TODO: handle non-sliding pieces (pawn, knight, king)

        return moves

    def _generate_sliding_moves(
        self, start_square: int, piece: int, moves: List[Move]
    ) -> None:
        """
        Generate sliding moves in all 8 directions for a piece.
        Stops on blocking pieces and adds captures for enemy pieces.
        """
        for direction_index in range(8):
            for n in range(self.num_squares_to_edge[start_square][direction_index]):
                target_square = start_square + DIRECTION_OFFSETS[direction_index] * (n + 1)
                piece_on_target = self.board.squares[target_square]

                if piece_on_target != Piece.None_:
                    # Capture if enemy piece
                    if not Piece.is_color(piece_on_target, self.board.color_to_move):
                        moves.append(Move(start_square, target_square))
                    break  # blocked by any piece

                moves.append(Move(start_square, target_square))
