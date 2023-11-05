from abc import ABC, abstractmethod
from logic import AN

class Piece(ABC): 
    def __init__(self, player: int) -> None:
        self._player = player

    @abstractmethod
    def __str__(self) -> str: ... 
    @abstractmethod
    def possible_moves(board, coord: AN) -> list[int]: ...


class King(Piece): 
    def possible_moves(board, coord: AN) -> list[int]:
        try: 
            # check right 
            pass
        except IndexError: 
            pass
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♚"
        else: 
            return "♔"

class Rook(Piece):
    def possible_moves(board, coord: AN) -> list[int]:
        pass
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♜"
        else: 
            return "♖"

class Bishop(Piece): 
    def possible_moves(board, coord: AN) -> list[int]:
        pass
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♝"
        else: 
            return "♗"

class Queen(Piece):
    def possible_moves(board, coord: AN) -> list[int]:
        pass
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♛"
        else: 
            return "♕"

class Knight(Piece):
    def possible_moves(board, coord: AN) -> list[int]:
        pass
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♞"
        else: 
            return "♘"

class Pawn(Piece): 
    def possible_moves(board, coord: AN) -> list[int]:
        pass
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♟"
        else: 
            return "♙"

class Empty: 
  def __str__(self) -> str: 
        return "·"