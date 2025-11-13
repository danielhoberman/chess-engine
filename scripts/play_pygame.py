import pygame
from chess.board import Board
from chess.piece import Piece
from chess.utils import load_position_from_fen, precompute_move_data
from chess.moveGenerator import MoveGenerator

pygame.init()

WIDTH, HEIGHT = 640, 640  # 8x8 board
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
MARGIN = 30  # Space for ranks/files

# Colors
WHITE = (245, 245, 220)
BLACK = (139, 69, 19)
HIGHLIGHT = (0, 255, 0)
TEXT_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH + MARGIN, HEIGHT + MARGIN))
pygame.display.set_caption("Chess")

# Font for ranks/files
font = pygame.font.SysFont('Arial', 20)

# ---------------------- Load Piece Images ----------------------
def load_images():
    pieces = ["P", "R", "N", "B", "Q", "K"]
    images = {}
    for piece in pieces:
        try:
            images[f"w{piece}"] = pygame.image.load(f"assets/w{piece}.png")
            images[f"b{piece}"] = pygame.image.load(f"assets/b{piece}.png")
            images[f"w{piece}"] = pygame.transform.scale(images[f"w{piece}"], (SQUARE_SIZE, SQUARE_SIZE))
            images[f"b{piece}"] = pygame.transform.scale(images[f"b{piece}"], (SQUARE_SIZE, SQUARE_SIZE))
        except FileNotFoundError:
            print(f"Image for {piece} not found. Skipping.")
    return images

images = load_images()

# ---------------------- Drawing Functions ----------------------
def draw_board(screen):
    """Draws chess board squares."""
    for file in range(ROWS):
        for rank in range(COLS):
            color = WHITE if (file + rank) % 2 == 0 else BLACK
            pygame.draw.rect(
                screen,
                color,
                (rank*SQUARE_SIZE + MARGIN, file*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            )

    # Draw ranks (1–8) **only on the left**
    for row in range(ROWS):
        rank_text = font.render(str(8 - row), True, TEXT_COLOR)
        screen.blit(rank_text, (5, row*SQUARE_SIZE + SQUARE_SIZE//2 - 10))  # Left side only

    # Draw files (a–h) on top and bottom
    files = ['a','b','c','d','e','f','g','h']
    for col in range(COLS):
        file_text = font.render(files[col], True, TEXT_COLOR)
        screen.blit(file_text, (col*SQUARE_SIZE + MARGIN + SQUARE_SIZE//2 - 5, HEIGHT))  # Bottom
        screen.blit(file_text, (col*SQUARE_SIZE + MARGIN + SQUARE_SIZE//2 - 5, 5))       # Top


def draw_pieces(screen, board_squares):
    for index, piece in enumerate(board_squares):
        if piece == Piece.None_:
            continue

        row = index // 8
        col = index % 8

        color_prefix = "w" if (piece & Piece.White) else "b"

        piece_type = piece & 0b111  # isolate lowest 3 bits for type
        symbol_map = {
            Piece.King: "k",
            Piece.Queen: "q",
            Piece.Rook: "r",
            Piece.Bishop: "b",
            Piece.Knight: "n",
            Piece.Pawn: "p",
        }

        symbol = symbol_map.get(piece_type)
        if symbol:
            image_key = f"{color_prefix}{symbol.upper()}"
            if image_key in images:
                screen.blit(
                    images[image_key],
                    (col * SQUARE_SIZE + MARGIN, row * SQUARE_SIZE),
                )


def highlight_square(screen, pos):
    row, col = pos
    pygame.draw.rect(
        screen,
        HIGHLIGHT,
        (col*SQUARE_SIZE + MARGIN, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
        5
    )

# ---------------------- Precompute Move Data ----------------------
num_squares_to_edge = precompute_move_data()  # called once, before the game loop

# ---------------------- Main Game Loop ----------------------
def main():
    start_fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

    board = Board()
    square = board.squares
    load_position_from_fen(start_fen, square)

    # Instantiate MoveGenerator with the board
    move_generator = MoveGenerator(board, num_squares_to_edge)

    # Generate moves
    moves = move_generator.generate_moves()

    selected_square = None
    running = True

    while running:
        screen.fill((200, 200, 200))  # Background for margins
        draw_board(screen)
        if selected_square is not None:
            highlight_square(screen, selected_square)
        draw_pieces(screen, square)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = (x - MARGIN) // SQUARE_SIZE
                row = y // SQUARE_SIZE

                if 0 <= row < 8 and 0 <= col < 8:
                    index = row * 8 + col

                    if selected_square is None:
                        selected_square = (row, col)
                    else:
                        src_index = selected_square[0] * 8 + selected_square[1]
                        piece = square[src_index]

                        if piece != Piece.None_:
                            square[index] = piece
                            square[src_index] = Piece.None_

                        selected_square = None

    pygame.quit()


if __name__ == "__main__":
    main()
