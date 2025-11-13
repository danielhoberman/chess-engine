from typing import Optional
from .piece import Piece


DIRECTION_OFFSETS = [8, -8, -1, 1, 7, -7, 9, -9]

def load_position_from_fen(fen: str, squares: list[int]) -> None:
    piece_type_from_symbol = {
        'k': Piece.King,
        'p': Piece.Pawn,
        'n': Piece.Knight,
        'b': Piece.Bishop,
        'r': Piece.Rook,
        'q': Piece.Queen,
    }

    fen_board = fen.split()[0]  # safer and cleaner than split(' ')[0]
    file = 0
    rank = 7

    for symbol in fen_board:
        if symbol == '/':
            file = 0
            rank -= 1
            continue

        if symbol.isdigit():
            file += int(symbol)
            continue

        # Piece placement
        color = Piece.White if symbol.isupper() else Piece.Black
        piece_type = piece_type_from_symbol.get(symbol.lower())

        if piece_type is None:
            raise ValueError(f"Invalid FEN symbol: '{symbol}'")

        index = rank * 8 + file
        squares[index] = piece_type | color
        file += 1


def precompute_move_data():
    num_squares_to_edge: list[Optional[list[int]]] = [None] * 64

    for file in range(8):
        for rank in range(8):
            num_north = 7 - rank
            num_south = rank
            num_west = file
            num_east = 7 - file

            square_index = rank * 8 + file

            num_squares_to_edge[square_index] = [
                num_north,
                num_south,
                num_west,
                num_east,
                min(num_north, num_west),  # NW
                min(num_south, num_east),  # SE
                min(num_north, num_east),  # NE
                min(num_south, num_west),  # SW
            ]

    return num_squares_to_edge





