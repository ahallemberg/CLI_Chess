from __future__ import annotations
from abc import ABC, abstractmethod
from src.coords import AN, ChessNotationError
from typing import Callable

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
    def possible_moves(self, coord: AN, board: dict[AN, Piece]) -> list[AN]: ...

    @property
    @abstractmethod
    def value(self) -> int: ...


class King(Piece): 
    @property
    def value(self) -> int: 
        return 1000
    
    def possible_moves(self, coord: AN, board: dict[AN, Piece]) -> list[AN]:
        coords: list[AN] = []
        for c_coord in coord.rel_coords((0, 1), (1,1), (-1, 1), (-1, 0), (1, 0), (0, -1), (-1,-1), (1, -1)): 
            if board[c_coord].player != self.player: 
                coords.append(c_coord)
        return coords

    def __str__(self) -> str: 
        if self._player == 0: 
            return "♚"
        else: 
            return "♔"
    
    def __repr__(self) -> str:
        return f"{self.__str__()}: {self._player}"
        
    
class Rook(Piece):
    @property 
    def value(self) -> int:
        return 5
    
    def possible_moves(self, coord: AN, board: dict[AN, Piece], ) -> list[AN]:
        # check horizontal and vertical
        return possible_moves_horizontal(coord, board) + possible_moves_vertical(coord, board)
    
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♜"
        else: 
            return "♖"
    
    def __repr__(self) -> str:
        return f"{self.__str__()}: {self._player}"
    

class Bishop(Piece): 
    @property
    def value(self) -> int:
        return 3
    
    def possible_moves(self, coord: AN, board: dict[AN, Piece]) -> list[AN]:
        return possible_moves_diagonals(coord, board)
    
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♝"
        else: 
            return "♗"
    
    def __repr__(self) -> str:
        return f"{self.__str__()}: {self._player}"
    

class Queen(Piece):
    @property
    def value(self) -> int:
        return 9
    
    def possible_moves(self, coord: AN, board: dict[AN, Piece]) -> list[AN]:
        return possible_moves_horizontal(coord, board) + possible_moves_vertical(coord, board) + possible_moves_diagonals(coord, board)
        
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♛"
        else: 
            return "♕"
        
    def __repr__(self) -> str:
        return f"{self.__str__()}: {self._player}"
    

class Knight(Piece):
    @property
    def value(self) -> int:
        return 3
    
    def possible_moves(self, coord: AN, board: dict[AN, Piece]) -> list[int]:
        coords: list[AN] = []

        for c_coord in coord.rel_coords((1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-2, 1), (-1, 2)): 
            if board[c_coord].player != self.player: 
                coords.append(c_coord)
            
        return coords

    def __str__(self) -> str: 
        if self._player == 0: 
            return "♞"
        else: 
            return "♘"
    
    def __repr__(self) -> str:
        return f"{self.__str__()}: {self._player}"


class Pawn(Piece): 
    @property
    def value(self) -> int:
        return 1
    
    def possible_moves(self, coord: AN, board: dict[AN, Piece]) -> list[AN]:
        coords: list[AN] = []
        if self.player == 0: 
            # go forward
            c_coord = coord.over()
            if isinstance(board[c_coord], Empty): 
                coords.append(c_coord)

            if coord.rank == 2: 
                c_coord = coord.over().over()
                if isinstance(board[c_coord], Empty): 
                    coords.append(c_coord)
        
            for c_coord in coord.rel_coords((1, 1),(-1, 1)): 
                if board[c_coord].player != self.player and not isinstance(board[c_coord], Empty): 
                    coords.append(c_coord)
        # check in front
        else: 
            # go backwards
            c_coord = coord.under()
            if isinstance(board[c_coord], Empty): 
                coords.append(c_coord)

            if coord.rank == 7: 
                c_coord = coord.under().under()
                if isinstance(board[c_coord], Empty): 
                    coords.append(c_coord)
        
            for c_coord in coord.rel_coords((1, -1),(-1, -1)): 
                if board[c_coord].player != self.player and not isinstance(board[c_coord], Empty): 
                    coords.append(c_coord)
        
        return coords
    
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♟"
        else: 
            return "♙"
    
    def __repr__(self) -> str:
        return f"{self.__str__()}: {self._player}"


class Empty(): 
    @property 
    def value(self) -> int: 
        return 0
    
    @property 
    def player(self) -> int: 
        return None
    
    def __str__(self) -> str: 
        return "·"

def coord_over(coord: AN) -> AN: 
    return coord.over()

def coord_under(coord: AN) -> AN: 
    return coord.under()

def coord_left(coord: AN) -> AN: 
    return coord.left()

def coord_right(coord: AN) -> AN: 
    return coord.right()

def coord_over_right(coord: AN) -> AN:
    return coord.over().right()

def coord_over_left(coord: AN) -> AN: 
    return coord.over().left()

def coord_under_left(coord: AN) -> AN: 
    return coord.under().left()

def coord_under_right(coord: AN) -> AN: 
    return coord.under().right()
    
def possible_moves_blc_piece(coord: AN, board: dict[AN, Piece], func: Callable[[AN], AN]) -> list[AN]: 
    coords: list[AN] = []
    try: 
        c_coord = coord
        while True: 
            c_coord = func(c_coord)
            if not isinstance(board[c_coord], Empty): 
                if board[c_coord].player != board[coord].player: 
                    coords.append(c_coord)
                break
            else: 
                coords.append(c_coord)

    except ChessNotationError: 
        pass 

    return coords

def possible_moves_horizontal(coord: AN, board: dict[AN, Piece]) -> list[AN]: 
    return possible_moves_blc_piece(coord, board, coord_left) + possible_moves_blc_piece(coord, board, coord_right)

def possible_moves_vertical(coord: AN, board: dict[AN, Piece]) -> list[AN]: 
    return possible_moves_blc_piece(coord, board, coord_over) + possible_moves_blc_piece(coord, board, coord_under)

def possible_moves_diagonals(coord: AN, board: dict[AN, Piece]) -> list[AN]:
        return possible_moves_blc_piece(coord, board, coord_over_left) + possible_moves_blc_piece(coord, board, coord_over_right) +  possible_moves_blc_piece(coord, board, coord_under_left) + possible_moves_blc_piece(coord, board, coord_under_right)
