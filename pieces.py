from __future__ import annotations
from abc import ABC, abstractmethod
from coords import AN, ChessNotationError

class Piece(ABC): 
    def __init__(self, player: int) -> None:
        self._player = player

    @property 
    def player(self) -> int: 
        return self._player 
    
    @player.setter 
    def player(self, val: int) -> None: 
        self._player = val

    @abstractmethod
    def __str__(self) -> str: ... 
    @abstractmethod
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[AN]: ...


class King(Piece): 
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[AN]:
        coords: list[AN] = []
        try: 
            left: Piece = board[coord.left()]
            right: Piece = board[coord.right()] 
            over: Piece = board[coord.over()]
            under: Piece = board[coord.under()]
            over_right: Piece = board[coord.over().right()]
            over_left: Piece = board[coord.over().left()]
            under_right: Piece = board[coord.under().right()]
            under_left: Piece = board[coord.under().left()]
            
            if left.player != self.player or isinstance(Empty, left):
                coords.append(coord.left())
            
            if right.player != self.player or isinstance(Empty, right):
                coords.append(coord.right())
            
            if over.player != self.player or isinstance(Empty, over): 
                coords.append(coord.over())
            
            if under.player != self.player or isinstance(Empty, under):
                coords.append(coord.under()) 

            if over_right.player != self.player or isinstance(Empty, over_right): 
                coords.append(coord.over().right())
            
            if over_left.player != self.player or isinstance(Empty, over_left):
                coords.append(over_left)
            if under_right.player != self.player or isinstance(Empty, under_right): 
                coords.append(under_right)

            if under_left.player != self.player or isinstance(Empty, under_left):
                coords.append(under_left)
            
            return coords
            
        except ChessNotationError: 
            pass

    def __str__(self) -> str: 
        if self._player == 0: 
            return "♚"
        else: 
            return "♔"

class Rook(Piece):
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[AN]:
        # check horizontal and vertical
        coords: list[AN] = []

        # check horozontal and diagonals
        for c_coord in coord.horizontal().extend(coord.vertical()): 
            if self.player != board[c_coord].player or isinstance(board[c_coord], Empty): 
                coords.append(c_coord)

    def __str__(self) -> str: 
        if self._player == 0: 
            return "♜"
        else: 
            return "♖"

class Bishop(Piece): 
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[AN]:
        coords: list[AN] = []

        for diagonal_coord in coord.diagonals(): 
            if board[diagonal_coord].player != self.player or isinstance(board[diagonal_coord], Empty): 
                coords.append(diagonal_coord)

        return coords
    
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♝"
        else: 
            return "♗"

class Queen(Piece):
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[AN]:
        coords: list[AN] = []

        c_coords = coord.horizontal()
        c_coords.extend(coord.vertical())
        c_coords.extend(coord.diagonals())
        # check horizontal and vertical and 
        for c_coord in c_coords: 
            if self.player != board[c_coord].player or isinstance(board[c_coord], Empty): 
                coords.append(c_coord)
        
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♛"
        else: 
            return "♕"

class Knight(Piece):
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[int]:
        pass
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♞"
        else: 
            return "♘"

class Pawn(Piece): 
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[AN]:
        coords: list[AN] = []
        if self.player == 0: 
            # go forward
            pass
        # check in front

        try: 
            pass

        except ChessNotationError: 
            pass

    def __str__(self) -> str: 
        if self._player == 0: 
            return "♟"
        else: 
            return "♙"

class Empty(): 
    @property 
    def player(self) -> int: 
        return None
    
    def __str__(self) -> str: 
        return "·"
  