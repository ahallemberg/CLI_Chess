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
        for c_coord in coord.rel_coords((0, 1), (1,1), (-1, 1), (-1, 0), (1, 0), (0, -1), (-1,-1), (1, -1)): 
            print(c_coord)
            if board[c_coord].player != self.player: 
                coords.append(c_coord)
        return coords

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
            if self.player != board[c_coord].player: 
                coords.append(c_coord)

    def __str__(self) -> str: 
        if self._player == 0: 
            return "♜"
        else: 
            return "♖"

class Bishop(Piece): 
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[AN]:
        coords: list[AN] = []

        for c_coord in coord.diagonals(): 
            if board[c_coord].player != self.player: 
                coords.append(c_coord)

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
            if self.player != board[c_coord].player: 
                coords.append(c_coord)
        
    def __str__(self) -> str: 
        if self._player == 0: 
            return "♛"
        else: 
            return "♕"

class Knight(Piece):
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[int]:
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

class Pawn(Piece): 
    def possible_moves(self, board: dict[AN, Piece], coord: AN) -> list[AN]:
        coords: list[AN] = []
        if self.player == 0: 
            # go forward
            c_coord = coord.over()
            if isinstance(board[c_coord], Empty): 
                coords.append(c_coord)

            if coord.file == "b": 
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

            if coord.file == "b": 
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

class Empty(): 
    @property 
    def player(self) -> int: 
        return None
    
    def __str__(self) -> str: 
        return "·"