import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, ROOT)

from board import Board
from square import Square
from move import Move
from piece import King


def test_starting_position_has_twenty_white_moves():
    board = Board()
    assert len(board.all_legal_moves('white')) == 20


def test_e2_to_e4_is_legal_for_white_pawn():
    board = Board()
    pawn = board.squares[6][4].piece
    board.calc_moves(pawn, 6, 4, bool=True)
    assert Move(Square(6, 4), Square(4, 4)) in pawn.moves


def test_kings_exist_at_start():
    board = Board()
    white_king = board.squares[7][4].piece
    black_king = board.squares[0][4].piece
    assert isinstance(white_king, King)
    assert isinstance(black_king, King)
