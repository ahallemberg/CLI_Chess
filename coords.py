from __future__ import annotations
from typing import overload

FILES = ["a","b","c","d","e","f","g","h"]
RANKS = [1,2,3,4,5,6,7,8]

class ChessNotationError(Exception):
    pass

class File(str) :
    def __add__(self, other: int) -> None: 
        try: 
            if FILES.index(self)+other > len(FILES)-1 or  FILES.index(self)+other < 0: 
                raise ChessNotationError
            
            return FILES[FILES.index(self)+other]
        except IndexError:
            raise ChessNotationError

class AN:
    """ 
    Algebraic notation for sjakk
    """
    @overload
    def __init__(self, coord: str) -> None: ...
    
    @overload
    def __init__(self, file: str, rank: int) -> None: ... 

    def __init__(self, file: str, rank: int|None=None) -> None: 
        if len(file) == 2: 
            if not self.valid_notation(file):
                raise ChessNotationError(f"{file} er en ugyldig algebraisk sjakknotasjon")
            self._coord = file

        elif len(file) == 1: 
            if not self.valid_notation(file, rank):
                raise ChessNotationError(f"file: {file}, rank: {rank} er en ugyldig algebraisk sjakknotasjon")
        
            self._coord = f"{file}{rank}"
            
        else: 
            raise ChessNotationError
     
    def __hash__(self) -> int:
        return hash(self._coord+"__AN")
    
    def __eq__(self, other: object) -> bool:
        return isinstance(other, AN) and self._coord == other.coord
    
    def __str__(self) -> str: 
        return f"AN({self._coord})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    @overload
    @staticmethod
    def valid_notation(file: str, rank: int) -> bool: ...

    @overload
    @staticmethod
    def valid_notation(coord: str) -> bool: ...
    
    @staticmethod
    def valid_notation(file: str, rank: int|None=None) -> bool: 
        if len(file) == 2: 
            try: 
                rank = int(file[1])
            except ValueError:
                return False 
            file = file[0]
        elif len(file) != 1: 
            raise ChessNotationError
        
        if file not in FILES: 
            return False
        if rank not in RANKS: 
            return False 
        return True
    
    def left(self) -> AN: 
        if self.file == FILES[0]:
            raise ChessNotationError
        return AN(FILES[FILES.index(self.file)-1], self.rank)
    
    def right(self) -> AN:
        if self.file == FILES[len(FILES)-1]:
            raise ChessNotationError
        return AN(FILES[FILES.index(self.file)+1], self.rank)

    def over(self) -> AN: 
        if self.rank == RANKS[len(RANKS)-1]:
            raise ChessNotationError
        return AN(self.file, RANKS[RANKS.index(self.rank)+1])

    def under(self) -> AN: 
        if self.rank == RANKS[0]:
            raise ChessNotationError
        return AN(self.file, RANKS[RANKS.index(self.rank)-1])
    
    def rel_coords(self, *deltas: tuple[int, int]) -> list[AN]: 
        coords: list[AN] = []
        for delta in deltas: 
            try: 
                new_coord = AN(self.coord)
                new_coord.file += delta[0]
                new_coord.rank += delta[1]
                coords.append(new_coord)

            except ChessNotationError: 
                pass
        
        return coords

    @property
    def coord(self) -> str: 
        return self._coord

    @coord.setter
    def coord(self, val: str) -> None: 
        if not self.valid_notation(val):
            raise ChessNotationError(f"{val} er en ugyldig algebraisk sjakknotasjon")
        self._coord = val
        
    @property
    def file(self) -> str: 
        return File(self._coord[0])

    @file.setter 
    def file(self, val: str) -> None: 
        if val in FILES: 
            self._coord = val + self._coord[1]
    
    @property 
    def rank(self) -> int:
        return int(self._coord[1])

    @rank.setter
    def rank(self, val: int) -> None: 
        if val in RANKS: 
            self._coord = self._coord[0] + str(val) 
